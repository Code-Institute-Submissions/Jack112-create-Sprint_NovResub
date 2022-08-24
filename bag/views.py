from django.shortcuts import render, redirect

def view_bag(request):
    """
    A view to render the bag template
    """

    context = {}

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """
    A view to add an item to the bag
    """

    bag = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')

    if item_id not in list(bag.keys()):
        bag[item_id] = item_id
        print('not in bag')
    else:
        print('already in bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_item(request, item_id):
    """
    A view to remove an item from the bag
    """

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        del bag[item_id]

    request.session['bag'] = bag
    return render(request, 'bag/bag.html')
