from django.shortcuts import render
from . forms import RegisterUserForm
# Create your views here.

def register(request):
    form  =RegisterUserForm
    return render(request, 'users/register.html', {'form': form})
