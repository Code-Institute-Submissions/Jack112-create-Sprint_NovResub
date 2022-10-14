from multiprocessing import context
from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def blog(request):
    """
    A view to render all blog posts
    """

    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blogs.html', context)


def single_blog(request, blog_id):
    """
    A view to render a single blog post
    """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog
    }
    return render(request, 'blog/single_blog.html', context)


@login_required
def add_blog(request):
    """
    A view to add a new blog post
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('blog')

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post successfully added')
            return (redirect('blog'))
        else:
            messages.error(
                request, 'Unable to add a new blog post at this time. Please try again later')
    else:
        form = BlogForm()

    context = {
        'form': form
    }

    return render(request, 'blog/add_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    """
    A view to edit a blog post
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('blog')

    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post successfully updated')
            return (redirect('blog'))
        else:
            messages.error(request, 'Unable to update blog post at this time. Please try again later')
    else:
        form = BlogForm(instance=blog)
        messages.info(
            request,
            f'''You are editing the following blog: {blog.name}'''
            )

    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, 'blog/edit_blog.html', context)


@login_required
def delete_blog(request, blog_id):
    """
    A view to delete a blog post
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect('blog')

    blog = get_object_or_404(Blog, pk=blog_id)

    blog.delete()
    messages.success(request, 'Blog successfully deleted!')
    return redirect('blog')
