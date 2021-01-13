from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'reuseable',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'description',
        'price',
        'image',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
