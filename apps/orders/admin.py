from django.contrib import admin

from apps.orders.models import Order, OrderItem

# Register your models here.

admin.site.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('total_price',)
    list_display = ('id', 'user', 'address', 'total_price', 'status')
    list_filter = ('status',)


admin.site.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('price',)
    list_display = ('id', 'order', 'product', 'quantity', 'price')