from django.shortcuts import render, get_object_or_404

from apps.products.models import Product
from apps.categories.models import Category

# Create your views here.

def product_list_view(request):
    category_id = request.GET.get('category')
    selected_category = None
    
    if category_id:
        selected_category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category_id=category_id).prefetch_related('images').order_by('-id')
    else:
        products = Product.objects.all().prefetch_related('images').order_by('-id')
        
    return render(request, 'products/product_list.html', {
        'products': products,
        'selected_category': selected_category
    })


def product_detail_view(request, product_id):
    product = get_object_or_404(Product.objects.prefetch_related('images'), id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})