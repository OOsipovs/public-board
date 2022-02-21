from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PostIt

@login_required()
def home_page(request):
    number_of_posts = PostIt.objects.filter(posted_by=request.user.id)
    context = {
        'post_its': PostIt.objects.all(),
        'number_of_personal_posts': len(number_of_posts)
    }

    return render(request, 'post/home.html', context)

@login_required()
def account_page(request):
    return render(request, 'post/account.html')

def about_page(request):
    return render(request, 'post/about.html')
