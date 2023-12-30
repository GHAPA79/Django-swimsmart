from django.contrib import admin

from . import models


@admin.register(models.MethodCategory)
class MethodCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.TypeSwimCategory)
class TypeSwimCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'method_category']


@admin.register(models.SeasonCategory)
class SeasonCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'method_category', 'type_swim_category']
    list_per_page = 16


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
