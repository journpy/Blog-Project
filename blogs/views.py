from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm


# Create your views here.
def index(request):
    """Retrieve data from the database."""
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    template = 'blogs/index.html' 
    return render(request, template, context)

def success(request):
    return render(request, 'blogs/success.html')


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(data=request.POST) 
        if form.is_valid():
            form.save(commit=True)
            return redirect('success')
    else:
        form = BlogForm()
        template = 'blogs/create_blog.html'
        context = {'form': form}
        return render(request, template, context)
    

    

