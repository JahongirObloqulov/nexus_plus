from django.contrib import admin
from .models import Category, City, Product, ProductImage
# Register your models here.
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Product)
admin.site.register(ProductImage)
