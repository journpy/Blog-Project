from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    """User signup view."""
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserCreationForm()
    context = {'form': form}
    return render(request, template_name='register.html', context=context)
