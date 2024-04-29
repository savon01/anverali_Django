from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from .views import logout_view, home, delete_user, edit_profile,\
    AboutMeView, RegisterView


app_name = 'myauth'

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',
         LoginView.as_view(
             template_name='myauth/login.html',
             redirect_authenticated_user=True,
         ),
         name='login'),
    path('logout/', logout_view, name='logout'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('delete-user/', delete_user, name='delete-user'),
    path('edit-profile/', edit_profile, name='edit-profile'),
]
