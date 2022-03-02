from django.shortcuts import render, redirect
from . forms import RegisterUsersForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterUsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUsersForm
    return render(request, 'users/register.html', {'form': form})
