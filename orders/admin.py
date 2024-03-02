from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'price']
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'phone_number', 'is_paid', 'datetime_modified']
    list_editable = ['is_paid']
    inlines = [OrderItemInline]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'price']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
