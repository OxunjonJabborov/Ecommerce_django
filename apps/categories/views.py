from django.shortcuts import render

from apps.categories.models import Category

# Create your views here.


def categories_list_view(request):
    main_categories = Category.objects.filter(parent=None).prefetch_related('subcategories')
    
    return render(request, 'categories/category_list.html', {'categories': main_categories})