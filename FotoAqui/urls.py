from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'FotoAqui'

urlpatterns = [
    path('',views.login_page,name='home'),
    path('my_images/',views.my_images,name='my_images'),
    path('my_books/',views.my_books,name='my_books'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('uploadbook/',views.login_page,name='uploadbook'),
    path('account/',views.account,name='account'),
    path('create_order/',views.create_order,name='create_order'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkout_complete/',views.CheckoutCompleteMsg,name = 'checkout_complete'),
    path("userCreated/", views.userCreated, name='userCreated'),

    path('register/create/',views.registerCreate,name='register_create'),
    path('login/',views.loginCreate,name='loginCreate'),
    path('logout/',views.logoutCreate,name='logoutCreate'),
    path('upload_img/', views.make_upload_img,name='upload_img'),
    path('checkout/complete_order/', views.completeOrder, name='complete_order'),
    path('start_account_activation/',views.start_account_activation, name = 'start_account_activation'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),

    path('test/',views.test_page,name='test_page'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
