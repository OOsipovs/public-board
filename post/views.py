from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def home_page(request):
    return render(request, 'post/home.html')

@login_required()
def account_page(request):
    return render(request, 'post/account.html')

def about_page(request):
    return render(request, 'post/about.html')
