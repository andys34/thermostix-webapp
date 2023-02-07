from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import Functions
import json

# Create your views here.


def Index(request):
    return render(request, "index.html")


def PushData(request):
    return HttpResponse(json.dumps([request.GET.get("id"),request.GET.get("temp"),request.GET.get("time")]))
