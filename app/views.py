from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    pro_obj = Product.objects.all()

    item_name = request.GET.get('item_name')
    if item_name != "" and item_name is not None:
        pro_obj = Product.objects.filter(title__icontains=item_name)        

    paginator = Paginator(pro_obj, 3)
    page = request.GET.get('page')
    pro_obj = paginator.get_page(page)


    context = {'pro_obj': pro_obj}
    return render(request, 'shop/index.html', context )

def detail(request, id):
    prod = Product.objects.get(id=id)

    context = {'prod': prod}
    return render(request, 'shop/detail.html', context )





