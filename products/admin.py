from django.contrib import admin
from .models import Product, Category

# Registered models here.
admin.site.register(Product)
admin.site.register(Category)