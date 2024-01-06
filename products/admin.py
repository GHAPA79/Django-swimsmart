from django.contrib import admin

from . import models


@admin.register(models.Category)
class MethodCategoryAdmin(admin.ModelAdmin):
    list_display = ['method_name', 'type_swimmer']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'number_of_sessions']
    list_editable = ['price']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'stars', 'active', 'datetime_modified']
    list_editable = ['active']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']
