
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='post-home'),
    path('account', views.account_page, name='post-account'),
    path('about', views.about_page, name='post-about'),
]
