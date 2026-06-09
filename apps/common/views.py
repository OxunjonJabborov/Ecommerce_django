from django.shortcuts import render

from apps.products.models import Product
from apps.categories.models import Category

# Create your views here.


def home_view(request):
    featured_products = Product.objects.all().order_by('-id')[:4]
    main_categories = Category.objects.filter(parent__isnull=True)
    
    context = {
        'products': featured_products,
        'categories': main_categories
    }
    return render(request, 'common/home.html', context)