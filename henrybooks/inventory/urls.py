from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('branches/', views.branch_list, name='branch_list'),
    path('inventory/', views.inventory_list, name='inventory_list'),
]
