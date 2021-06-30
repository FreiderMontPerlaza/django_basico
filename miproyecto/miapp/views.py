from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'miapp/index.html')

def product(request):
   return render(request,'miapp/product.html')

def contact(request):
    return render(request,'miapp/contact.html')

def galeria(request):
    return render(request,'miapp/galeria.html')