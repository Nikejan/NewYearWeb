from django.contrib import admin
from .models import *
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
admin.site.register(Product, ProductAdmin)



