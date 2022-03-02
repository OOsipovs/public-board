from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PostIt
from .forms import PostItForm

@login_required()
def home_page(request):

    if request.method == "POST":
        form = PostItForm(request.POST)
        form.instance.posted_by = request.user

        if form.is_valid():
            form.save()
            return redirect('post-home')
    else:
        form = PostItForm()


    number_of_posts = PostIt.objects.filter(posted_by=request.user.id)
    context = {
        'post_its': PostIt.objects.order_by('-posted_date'),
        'number_of_personal_posts': len(number_of_posts),
        'form': form
    }

    return render(request, 'post/home.html', context)

@login_required()
def account_page(request):
    return render(request, 'post/account.html')

def about_page(request):
    return render(request, 'post/about.html')
