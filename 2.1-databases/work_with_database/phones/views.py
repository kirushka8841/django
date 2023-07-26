from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort')
    catalog = Phone.objects.all()
    if sort_param == 'name':
        catalog = catalog.order_by('name')
    elif sort_param == 'min_price':
        catalog = catalog.order_by('price')
    elif sort_param == 'max_price':
        catalog = catalog.order_by('price').reverse()
    context = {
        'phones': catalog
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    catalog_phone = Phone.objects.get(slug=slug)
    context = {
        'phone': catalog_phone
    }
    return render(request, template, context)
