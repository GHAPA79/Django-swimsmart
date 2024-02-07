from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['method_name', 'type_swimmer']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_id', 'category', 'price', 'number_of_sessions', 'duration']
    list_per_page = 12


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user']
