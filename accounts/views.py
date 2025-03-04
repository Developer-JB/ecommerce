from django.shortcuts import render,redirect
from . forms import CreateUserForm

# Create your views here.

def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request,'accounts/register.html',context)

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    pass