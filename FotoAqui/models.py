from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class Account(AbstractUser):
    isPhotogapher = models.BooleanField(default=False)
    cpf = models.CharField(max_length=14)
    data_nasc = models.DateField(auto_now=False, null=True)
    img_perfil = models.ImageField(upload_to='imgs/perfis/%Y',null=False, default="SEM-IMAGEM")

    def __str__(self):
        return str(self.username)

class HomeComments (models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    stars = models.IntegerField(default=5)
    comment = models.CharField(max_length=320)

class Business_model (models.Model):
    title = models.CharField(max_length=254, default='sem_nome')
    img_price = models.FloatField(default=5.0, null=False, blank= False, )
    active = models.BooleanField(default=False)
    expiration_time = models.IntegerField(default=15)
#    img_price = models.DecimalField(default=2.5, decimal_places=2,max_digits=6)



class Load (models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    photographer = models.ForeignKey(Account,null=True, on_delete=models.SET_NULL)
    client = models.EmailField(max_length=254,null=True)

    @property
    def numberOfImages(self):
        return Image.objects.filter(load = self).count()
    
    @property
    def numberOfLikes(self):
        return Image.objects.filter(load = self, like = True).count()
    
    @property
    def numberOfDislikes(self):
        return Image.objects.filter(load = self, dislike = True).count()

class Order (models.Model):
    account = models.ForeignKey(Account,null=True,blank=True ,default=None,on_delete=models.SET_DEFAULT)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)
    qtd_imgs = models.IntegerField(default=0, null=True, blank=True)
        
    
class Image (models.Model):
    photo_img = models.ImageField(upload_to = 'imgs/%Y%M%D',null=True, blank=True, default='default.jpeg')
    filename = models.CharField(max_length=254,null=False,default='img_Sem_Nome')
    ordered = models.BooleanField(default=False)
    client_email =models.EmailField(null=False)
    photographer = models.CharField(null=True,blank=True,max_length=254)
    created_at = models.DateField(auto_now_add=True)
    load = models.ForeignKey(Load,on_delete=models.CASCADE, null=True,blank=True)
    order = models.ForeignKey(Order, null=True,blank=True,on_delete=models.SET_NULL)
    expiration_date = models.DateField(default=datetime.date.today)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)




