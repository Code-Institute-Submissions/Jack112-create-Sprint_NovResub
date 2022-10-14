from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Function to render bar items
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id in bag:
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        product_count = len(bag)
        bag_items.append({
            'item_id': item_id,
            'product': product
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
