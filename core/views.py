from django.shortcuts import render
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

@login_required
def profile(request):
    print(request.user)
    return render(request, 'profile.html', {'username': request.user})