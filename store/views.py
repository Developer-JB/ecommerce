from django.shortcuts import render
from . models import Category,Product

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'store.html',context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}
