from django.shortcuts import render

def handler404(request, exception):
    """ Error Handler 404 - View to render 404 page"""
    return render(request, "errors/404.html", status=404)


def handler500(request, *args, **argv):
    """ Error Handler 500 - View to render 500 page"""
    return render(request, "errors/500.html", status=500)
