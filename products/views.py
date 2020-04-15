from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


# Create your views here.
# /products call this function
def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('This is a new file')

