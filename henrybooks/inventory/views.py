from django.shortcuts import render
from .models import Book, Branch, Inventory

def home(request):
    return render(request, 'inventory/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'inventory/book_list.html', {'books': books})

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'inventory/branch_list.html', {'branches': branches})

def inventory_list(request):
    inventory = Inventory.objects.select_related('book', 'branch').all()
    return render(request, 'inventory/inventory_list.html', {'inventory': inventory})
