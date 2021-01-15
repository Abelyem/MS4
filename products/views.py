from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """A view to return all products - search and sorting included """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def mask_detail(request, mask_id):
    """A view to return an individually selected mask """

    mask_detail = get_object_or_404(Product, pk=mask_id)

    context = {
        'mask_detail': mask_detail,
    }

    return render(request, 'products/mask_detail.html', context)
