from django.contrib import admin
from .models import Account, HomeComments, Image,Load,Business_model,Order,Wallet,Operation
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin (UserAdmin):

    list_display = (
        'id',
        'username',
        'isPhotogapher',
    )
    list_display_links = (
        'id',
        'username',
    )
    list_editable = (
        'isPhotogapher',
    )
class OrderAdmin (admin.ModelAdmin):
    list_display=(
        'id',
        'account',
        'ordered',
    )

class HomeCommentsAdmin(admin.ModelAdmin):
    ...

class ImageAdmin(admin.ModelAdmin):
    list_display=(
        'client_email',
        'ordered',
        'like',
        'dislike',
        'created_at',
    )
    list_editable = (
        'ordered',
        'like',
        'dislike',
    )

class LoadAdmin(admin.ModelAdmin):
    ...

class Business_modelAdmin(admin.ModelAdmin):
    ...

class WalletAdmin(admin.ModelAdmin):
    list_display=(
        'account',
        'value',
    )
class OperationAdmin(admin.ModelAdmin):
    ...


admin.site.register(Operation,OperationAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Business_model,Business_modelAdmin)
admin.site.register(Load,LoadAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(HomeComments,HomeCommentsAdmin)