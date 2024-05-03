
from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('events',views.add_events,name='events'),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete_product,name="delete"),
    path('register/',views.register,name="register"),
    path('login/',views.user_login,name="login"),
    path('login/',views.user_logout,name="logout"),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('schedule/', views.schedule, name='schedule'),
    path('blog/', views.blog, name='blog'),
    path('price/', views.price, name='price'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),

] 

