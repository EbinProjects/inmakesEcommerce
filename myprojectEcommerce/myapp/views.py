from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def allProdCat(request, c_slug=None):
    c_page = None
    products = None
    if c_slug:
        c_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.filter(category=c_page, available=True)
    else:
        product = Product.objects.all().filter(available=True)
        pageInitor = Paginator(product, 6)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            products = pageInitor.page(page)
        except (InvalidPage, EmptyPage):
            products = pageInitor.page(pageInitor.num_pages)
    return render(request, 'category.html', {'category': c_page, 'products': products})


def allProductDetails(request, c_slug, producr_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=producr_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})
