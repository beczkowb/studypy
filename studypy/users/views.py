from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .forms import LoginForm


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('newest')
        else:
            return render(request, 'users/login.html', {'form': form})