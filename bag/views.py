from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """A view to return the shopping bag contents --
    from boutique ado with slight amendments """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
