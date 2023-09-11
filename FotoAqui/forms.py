from django import forms
from .models import *
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):

    password_conf = forms.CharField(
        required=True,
        widget= forms.PasswordInput(attrs={
            'class':'inputTextStyle',
            'type':'password',
            'placeholder':'Senha',
            'id':'reg_id_password_conf',
        })
    )

    acept_terms = forms.BooleanField(
        required=True,
        widget= forms.CheckboxInput(attrs={
            'class':'checkBox_acept_terms',
            'id':'checkBox_acept_terms',
        })
    )

    class Meta:
        model = Account
        fields = [
            'email',
            'username',
            'password',
            'password_conf',
            
        ]
        widgets = {
            'username': forms.TextInput(attrs={
            'class':'inputTextStyle',
            'id':'reg_id_username',
            }),
            'email': forms.TextInput(attrs={
            'class':'inputTextStyle',
            'id':'reg_id_email',
            }),
            'password': forms.TextInput(attrs={
            'class':'inputTextStyle',
            'type':'password',
            'placeholder':'Senha',
            'id':'reg_id_password',
            }),
        }
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_conf = cleaned_data.get('password_conf')
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')

        email_exists = Account.objects.filter(email=email).exists()
        username_exists = Account.objects.filter(username=username).exists()

        if username_exists:
            raise ValidationError('Este usuario ja esta em uso! [forms]')

        if email_exists:
            raise ValidationError('Este email ja esta em uso! [forms]')

        if password != password_conf:
            raise ValidationError(
                'As senhas não são iguais [forms]'
            )



class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
            'class':'inputTextStyle',
            'placeholder':'Email...',
            }),
            'password': forms.TextInput(attrs={
            'class':'inputTextStyle',
            'type':'password',
            'placeholder':'Senha',
            })
        }
    def clean(self):
        ...

class ImageLoadForm (forms.ModelForm):

    class Meta:
        model = Image
        fields = [
            'client_email',
            'photo_img',
            'photographer',
            'load',
            'ordered',
            
        ]
        widgets = {
            'photo_img': forms.FileInput(attrs={
                'class':'imgInput',
                'id':'imgs',
                #'multiple':True,
            }
            ),
        
            'client_email': forms.EmailInput(attrs={
                'placeholder':'Email do cliente',
                'class':'no-show',
                'name':'btn_upload_file',
            }
            ),
            
        }
    def clean(self):
        ...


class UpdateInformationForm (forms.ModelForm):

    class Meta:
        model = Account
        fields = [
            'img_perfil',
            'username',
            'email',
            'first_name',
            'last_name',
            'data_nasc',
            'cpf',
            
        ]
        widgets = {
        
            'email': forms.EmailInput(attrs={
                'class':'inputTextStyle',
                'name':'email',
            }
            ),

            'username': forms.TextInput(attrs={
                'class':'inputTextStyle',
                'name':'Username',
            }
            ),
            'first_name': forms.TextInput(attrs={
                'class':'inputTextStyle',
                'name':'first Name',
            }
            ),
            'last_name': forms.TextInput(attrs={
                'class':'inputTextStyle',
                'name':'last Name',
            }
            ),
            'cpf': forms.TextInput(attrs={
                'class':'inputTextStyle',
                'name':'cpf',
            }
            ),
            
            
        }
    def clean(self):
        ...

