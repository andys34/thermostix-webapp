from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import Functions
import json
from thermostixapp.models import User, Thermometer, Log
from datetime import datetime

# Create your views here.


def Index(request):
    users = User.objects.all().values()
    thermometers = Thermometer.objects.all()
    if users == None:
        users = []
    if thermometers == None:
        thermometers = []
    thermometersData = []
    for therm in thermometers:
        temps = Log.objects.filter(thermometer=therm).values
        thermometersData.append({"id": therm.id, "temps": temps, "dates": []})
    return render(
        request, "index.html", {"users": users, "thermometers": thermometersData}
    )


def AdminView(request):
    users = User.objects.all().values()
    thermometers = Thermometer.objects.all().values()
    if users == None:
        users = []
    if thermometers == None:
        thermometers = []
    return render(request, "admin.html", {"users": users, "thermometers": thermometers})


def PushData(request):
    log = Log(
        temperature=request.GET.get("temp"),
        thermometer=Thermometer.objects.get(id=request.GET.get("id")),
        time=datetime.fromtimestamp(int(request.GET.get("time"))),
    )

    log.save()
    return HttpResponse("Logged.")


def AddUser(request):
    user = User(username=request.GET.get("username"))
    user.save()
    return HttpResponse("User added.")


def AddThermometer(request):
    thermometer = Thermometer()
    thermometer.save()
    return HttpResponse("Thermometer added.")


def AssignThermometersToUser(request):
    thremometer = Thermometer.objects.get(id=request.GET.get("thermometerId"))
    user = User.objects.get(username=request.GET.get("username"))
    if thremometer.assignedUsers.filter(username=user.username).exists():
        return HttpResponse("User already is assigned this thermometer!")
    thremometer.assignedUsers.add(user)
    thremometer.save()
    return HttpResponse("Done.")
