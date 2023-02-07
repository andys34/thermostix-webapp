from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import Functions

# Create your views here.


def Index(request):
    return render(request, "index.html")
