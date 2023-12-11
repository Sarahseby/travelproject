from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('tem', views.tem, name='tem'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    ]