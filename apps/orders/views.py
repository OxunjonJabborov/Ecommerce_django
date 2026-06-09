from django.shortcuts import render, get_object_or_404

from apps.orders.models import Order, OrderItem

# Create your views here.

def order_list_view(request):
    user_orders = Order.objects.filter(user_id=1).order_by('-id')
    return render(request, 'orders/order_list.html', {'orders': user_orders})

def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()

    context = {
        'order': order,
        'items': order_items
    }
    return render(request, 'orders/order_detail.html', context)