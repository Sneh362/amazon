from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Product
from .forms import LoginForm

# In-memory user store (for simplicity)
# users = {'1': '1'}
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # if users.get(username) == password:
#         #     request.session['user'] = username
#         return redirect('add_product')
#     return render(request, 'login.html')

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # Simulate a successful login
#             return redirect('add_product')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# def add_product_view(request):
#     if 'user' not in request.session:
#         return redirect('login')
    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         category = request.POST.get('category')
#         Product.objects.create(name=name, price=price, category=category)
        
#     products_list = Product.objects.all()
#     paginator = Paginator(products_list, 5)  # Show 5 products per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     return render(request, 'add_product.html', {'page_obj': page_obj})

# def product_list_view(request):
#     query = request.GET.get('q')
#     if query:
#         products_list = Product.objects.filter(name__icontains=query)
#     else:
#         products_list = Product.objects.all()
    
#     paginator = Paginator(products_list, 5)  # Show 5 products per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     return render(request, 'product_list.html', {'page_obj': page_obj})

from django.shortcuts import render, redirect
from .forms import ProductForm, LoginForm
from .models import Product
from django.core.paginator import Paginator

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Simulate a successful login
            return redirect('add_product')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_list_view(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query)
    
    paginator = Paginator(products, 15)  # Show 5 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'page_obj': page_obj})
