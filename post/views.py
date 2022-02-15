from django.shortcuts import render

def home_page(request):
    return render(request, 'post/home.html')

def account_page(request):
    return render(request, 'post/account.html')

def about_page(request):
    return render(request, 'post/about.html')
