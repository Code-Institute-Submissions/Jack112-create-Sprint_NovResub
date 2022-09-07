from django.shortcuts import render

def profile(request):
    """
    A view to render the users profile
    """
    return render(request, 'profiles/profile.html')

