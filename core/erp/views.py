from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.erp.models import Category,Product


def myfirstview(request):
    data = {"name": "Alexander",
            'category': Category.objects.all()
             }
    
    return render(request, "index.html", data)


def mysecondview(request):
    data = {"name": "Alexander",
            'productos': Product.objects.all()
             }
    
    return render(request, "second.html", data)
