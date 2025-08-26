from django.shortcuts import render, get_object_or_404

from .models import Products


# Create your views here.
def homepage(request):
    products = Products.objects.filter(main_window_display=True)
    return render(request, 'index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'product.html', {'product': product})
