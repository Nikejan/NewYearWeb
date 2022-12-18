from django.contrib import admin
from .models import *
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "image_url")
admin.site.register(Product, ProductAdmin)



