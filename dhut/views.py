from django.shortcuts import render
from django.http import HttpResponse

from .models import Measurement

# List of all measurements as index page
def index(request):
    measurements = Measurement.objects.all().order_by('-id')[:200]
    return render(request, "db.html", {"measurements": measurements})

# Add a measurement
def add(request):
    measurement = Measurement()
    measurement.when = request.GET['when']
    measurement.temp = request.GET['temp']
    measurement.rh   = request.GET['rh']
    measurement.save()

    return HttpResponse('')
