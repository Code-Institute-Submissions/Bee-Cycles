from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return index.html and fetching all products,
    new_arrivals and deals are shown on index.html """
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)
