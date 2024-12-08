from django.shortcuts import render,get_object_or_404
from . models import Category,Product

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'store/store.html',context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def product_info(request,slug):
    products=get_object_or_404(Product,slug=slug)

    context = {'products':products}
    return render(request,'store/product_info.html',context)

def list_categories(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=Product.objects.filter(category=category)

    return render(request,'store/list_categories.html',{'categories':categories, 'products':products})
