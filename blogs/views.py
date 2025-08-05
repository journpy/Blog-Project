from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Retrieve data from the database."""
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    template = 'blogs/index.html' 
    return render(request, template, context)


@login_required
def success(request):
    return render(request, 'blogs/success.html')

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(data=request.POST) 
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return redirect('success')
    else:
        form = BlogForm()
        template = 'blogs/create_blog.html'
        context = {'form': form}
        return render(request, template, context)
    

@login_required   
def blog_detail(request, blog_id):
    """Detail View for a blog"""
    blog = Blog.objects.get(id=blog_id)
    if blog.author != request.user:
        raise Http404
    context = {'blog': blog}
    template = 'blogs/blog_detail.html'
    return render(request, template, context)


@login_required
def update_blog(request, blog_id):
    """Update a blog."""
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        raise Http404
    
    if request.method == 'POST':
        form = BlogForm(data=request.POST, instance=blog)
        if form.is_valid():
            edit_blog = form.save(commit=False)
            #edit_blog.author = request.user
            edit_blog.save()
            return redirect('blog-detail', blog.id)
    else:
        form = BlogForm(instance=blog)
        return render(request, template_name='blogs/update_blog.html', context={'form': form})
    

@login_required
def delete_blog(request, blog_id):
    """Delete a blog."""
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        raise Http404
    if request.method == 'POST':
        blog.delete()
        return redirect('index')
    context = {'blog': blog}
    return render(request, template_name='blogs/delete_blog.html', context=context)

    

    

