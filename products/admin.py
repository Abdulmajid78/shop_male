from django.contrib import admin
from .models import *


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'discount']
    list_display_links = ['id', 'title', 'price', 'discount']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ProductCategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(ProductTagModel)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(ProductColorModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'code']
    list_display_links = ['id', 'code']
    search_fields = ['code']
