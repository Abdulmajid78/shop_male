from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from .forms import ColorForm


@admin.register(ProductBrandModel)
class ProductBrandModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'real_price', 'price', 'discount']
    list_display_links = ['id', 'title', 'price', 'discount']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['real_price']


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
    list_display = ['id', 'get_code', 'code']
    list_display_links = ['id', 'code']
    search_fields = ['code']
    form = ColorForm

    def get_code(self, obj):
        text = '&nbsp'
        return mark_safe(
            f'<p style="background-color: {obj.code}; width:120px;border:1px solid black">{text}</p>')
