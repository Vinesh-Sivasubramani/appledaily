from django.shortcuts import render
from .models import Product

# Create your views here.

def collection(request):
    product=Product.objects.all()
    context = {'product':product}
    return render(request,'shop/collections.html',context)


def blog(request,pk):
    blog = Product.objects.get(name=pk)
    context = {'blog':blog}
    return render(request,'shop/blog.html',context)

def about(request):
   
    return render(request,'shop/about.html')