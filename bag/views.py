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

    bag['item_id'] = item_id

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
