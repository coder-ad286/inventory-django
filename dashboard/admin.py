from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group

admin.site.site_header = "AD Inventory Dashboard"

#CHANGE LISTING
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
# class OrderAdmin(admin.ModelAdmin):
#     list_display=('product','staff','order_quantity')
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)

# admin.site.unregister(Group)
