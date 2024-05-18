"""
URL configuration for bookwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [
    path('', views.index),
    path('books/', views.getBooks),
    path('book/<int:bId>', views.book,name='book'),
    path('contactus/', views.getContactus),
    path('aboutus/', views.getAboutus),
    path('addpc/', views.add_pc),
    path("update/<int:bId>", views.update_pc),
    path('success/',views.success ,name="success"),
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:pc_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete-purchase/', views.complete_purchase, name='complete_purchase'),

]    

    


