from django.contrib import admin

from .models import Categories, Brands, Products, Variations


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'seo_title', 'seo_description', 'slug', 'isActive')
    search_fields = ('name', 'seo_title', 'seo_description', 'slug')
    list_filter = ('isActive', 'name')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'seo_title', 'seo_description', 'slug')
    search_fields = ('name', 'seo_title', 'seo_description', 'slug')
    list_filter = ('name',)


class InlineVariation(admin.TabularInline):
    model = Variations
    extra = 1


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'brand', 'date', 'price', 'discount_price', 'slug', 'isActive')
    search_fields = ('name', 'category', 'brand')
    list_filter = ('isActive', 'category', 'brand')
    inlines = [InlineVariation]


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'price', 'discount_price')
    search_fields = ('product', 'name')
    list_filter = ('product',)


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Brands, BrandAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Variations, VariationAdmin)
