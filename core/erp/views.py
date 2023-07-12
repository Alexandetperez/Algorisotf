from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def myfirstview(request):
    data = {"name": "Alexander"}
    return render(request, "index.html", data)
