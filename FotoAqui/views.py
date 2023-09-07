from django.shortcuts import render, redirect
from .forms import ImageLoadForm, LoginForm, RegisterForm, UpdateInformationForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import random
import json
from datetime import datetime, timedelta

#Activation email Imports...
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth import get_user_model


#---------------Responses---------------------#
def test_page (request):
    img = Image.objects.filter(client_email = 'eliveltonalmeidapardini@gmail.com').first()

    return render(request,'Pages/test_page.html',{
        'img':img,
    })


def login_page (request):
    registerForm = RegisterForm()
    loginForm = LoginForm()
    comments = list(HomeComments.objects.all())
    if request.user.is_authenticated:
        info = Account.objects.get(username = request.user)
    else:
        info =None
    if (len(comments)>3):
        comments = random.sample(comments,3)

    return render(request, 'Pages/home.html', {
        'info':info,
        'registerForm' : registerForm,
        'loginForm' : loginForm,
        'comments':comments,
    })
def dashboard(request):

    info = Account.objects.get(username = request.user)
    loads = Load.objects.filter(photographer = info)
    if(info.isPhotogapher == False):
        return redirect('FotoAqui:home')


    image_load = ImageLoadForm()

    return render(request, 'Pages/dashboard.html',{
        'image_load':image_load,
        'loads':loads,
        'info':info,
    })
@login_required(login_url='FotoAqui:Home',redirect_field_name='next')
def my_images(request):
    info = Account.objects.get(username = request.user)
    imgs = Image.objects.filter(client_email = info.email,ordered = False).order_by('load')
    business = Business_model.objects.get(active = True)
    return render(request, 'Pages/my_images.html',{
        'info':info,
        'imgs':imgs,
        'business':business,
    })
@login_required(login_url='FotoAqui:home',redirect_field_name='next')
def my_books (request):
    info = Account.objects.get(username = request.user)
    imgs = Image.objects.filter(client_email =info.email, ordered = True).order_by('load')
    return render(request, 'Pages/my_books.html',{
        'info':info,
        'imgs':imgs,
    })

#DOING =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
@login_required(login_url='FotoAqui:home',redirect_field_name='next')
def account (request):
    account_form = UpdateInformationForm()
    info = Account.objects.get(id= request.user.id)
    return render(request, 'Pages/account.html',{
        'account_form':account_form,
        'info':info,
        }
    )
@login_required(login_url='FotoAqui:home', redirect_field_name='next')
def account_update(request):
    if not request.POST:
        raise Http404
    else:
        info = Account.objects.get(user = request.user)
        
#DOING =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

@login_required(login_url='FotoAqui:home',redirect_field_name='next')
def checkout(request):
    if not request.POST:
        info = Account.objects.get(username = request.user)
        order = Order.objects.filter(account = request.user,ordered=False).first()
        imgs = Image.objects.filter(client_email = info.email,ordered = False, order = order)
        business  =Business_model.objects.filter(active = True).first()
        return render(request, 'Pages/checkout_page.html',{
            'info': info,
            'order':order,
            'imgs':imgs,
            'business':business,
        })
    else:
        print('request post')
        return JsonResponse('Indo para checkout',safe=False)
    
def create_order (request):
    data = json.loads(request.body)
    account = Account.objects.get(username = request.user)
    in_cart = data['in_cart_list']
    Order.objects.filter(account = request.user, ordered = False).delete()
    order = Order.objects.create(account = request.user, ordered = False)
    itens_to_add = Image.objects.filter(id__in=in_cart, client_email = account.email)

    for iten in itens_to_add:
        iten.order = order
    Image.objects.bulk_update(itens_to_add,['order'])
    #colocar valor da quantidade e salvar
    order.qtd_imgs = itens_to_add.count()
    order.save()
    return JsonResponse('tamo matutando!',safe=False)

@login_required(login_url='FotoAqui:home',redirect_field_name='next')
def upload_viwer(request):
    return render(request,'Pages/TEST.html')
def userCreated (request):
    return render(request, 'Pages/userCreated.html')


@login_required(login_url='FotoAqui:home', redirect_field_name='next')
def CheckoutCompleteMsg(request):
    info = Account.objects.get(username = request.user)
    return render(request, 'Pages/checkout_complete.html',{
        'info':info,
    })

def start_account_activation (request):
    return render(request, 'Pages/start_account_activation.html')

#---------------Redirects---------------------#

def registerCreate (request):
    if not request.POST:
        raise Http404()
    else:
        POST = request.POST
        request.session['register_form_data'] = POST
        form = RegisterForm(POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(user.password)
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            del(request.session['register_form_data'])
            #messages.success(request,'Usuario criado com sucesso Hora de Logar!')
            return redirect('FotoAqui:start_account_activation')
        else:
            messages.error(request,'Falha ao Criar usuario')

        return redirect('FotoAqui:home')
    

def loginCreate (request):
    if not request.POST:
        raise Http404()
    else:
        form = LoginForm(request.POST)

        if form.is_valid():
            is_authenticated = authenticate(
                username = form.cleaned_data.get('username',''),
                password = form.cleaned_data.get('password',''),
                )
            
            if is_authenticated is not None:
                messages.success(request,'Login efetuado com sucesso!!!')
                login(request,is_authenticated)
                my_Account = Account.objects.get(username = request.user)
                if my_Account.isPhotogapher:
                    return redirect('FotoAqui:dashboard')
                return redirect('FotoAqui:my_images')
            messages.error(request, 'credenciais Invalidas')
    return redirect('FotoAqui:home')

@login_required(login_url='FotoAqui:home')
def logoutCreate(request):
    logout(request)
    return redirect('FotoAqui:home')

@login_required(login_url='FotoAqui:home')
def completeOrder (request):
    print('Passou Aqui')
    body = json.loads(request.body)
    order = Order.objects.get(id = body['order_id'])
    order.ordered = True
    order.save()

    to_pay = Image.objects.filter(order = order)
    
    for img in to_pay:
        photographer = Account.objects.get(username = img.photographer)
        wallet = Wallet.objects.get(account = photographer)
        new_value = wallet.value+Business_model.objects.get(active = True).img_price
        wallet.value = new_value
        wallet.save()

    Image.objects.filter(order = order).update(ordered = True)
    messages.success(request,'Pagamento confirmado com sucesso!')
    return redirect('FotoAqui:home')



def make_upload_img(request):
    if not request.POST:
        raise Http404()
    
    form = ImageLoadForm(request.POST,request.FILES)
    img_list = []

    if (form.is_valid()):
        
        load = Load.objects.create(photographer=request.user,client = request.POST['client_email'].lower())
        load.save()
        client_account = Account.objects.get(email=request.POST['client_email'].lower())
        businessmodel = Business_model.objects.filter(active = True).first()

        for img in request.FILES.getlist('photo_img'):
            img_list.append(
                Image(
                    photo_img = img,
                    photographer = request.user,
                    client_email = request.POST['client_email'].lower(),
                    load = load,
                    ordered = False,
                    expiration_date = datetime.today() + timedelta(businessmodel.expiration_time),
                #filename = f'img_{}'
                )
            )
        print('>>>>>VVV>>>>>')
        print(img_list)
        print(request.FILES)
        Image.objects.bulk_create(img_list)
        messages.success(request, 'imagens carregadas!')
        sendEmail_notification(request, client_account,client_account.email)
        return redirect('FotoAqui:dashboard')
    else:
        messages.error(request,'ops... algo deu errado por favor tente novamente mais tarde')
        print('<<<<<<<<<< DEU RUIM PATRAO! >>>>>>>>>')
        print(form.errors)
        return redirect('FotoAqui:dashboard')


def sendEmail_notification(request, user, to_email):
    mail_subject = "Voce tem novas fotos em FotoAqui!"
    message = render_to_string('MailTemplates/newEmailNotification.html', {
        'user':user.username,
        'domain': get_current_site(request).domain,
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject,message, to=[to_email])
    if email.send():
        ...
    else:
        print('erro email nao pode ser enviado')

#move this to Utils sometime -- é apenas a funçao que começa o processo de ativaçao do email!
def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('MailTemplates/emailActivationTemplate.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        ...
    else:
       messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')



def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        #messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('FotoAqui:userCreated')
    else:
        messages.error(request, 'Activation link is invalid!')
    
    return redirect('FotoAqui:home')
...