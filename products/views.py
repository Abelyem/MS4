from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """A view to return all products - search and sorting included """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(colour__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query
    }

    return render(request, 'products/products.html', context)


def mask_detail(request, mask_id):
    """A view to return an individually selected mask """

    mask_detail = get_object_or_404(Product, pk=mask_id)

    context = {
        'mask_detail': mask_detail,
    }

    return render(request, 'products/mask_detail.html', context)
