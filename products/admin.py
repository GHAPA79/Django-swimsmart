from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['method_name', 'type_swimmer']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category_id', 'category', 'price', 'number_of_sessions', 'duration']
    list_per_page = 12


@admin.register(models.PurchaseFile)
class PurchaseFileAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'datetime_modified']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']
