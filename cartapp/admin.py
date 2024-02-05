from django.contrib import admin

from cartapp.models import Cart

# Register your models here.
class Manage(admin.ModelAdmin):
    list_display=['customer','cart_id']

admin.site.register(Cart,Manage)
