from django.shortcuts import render
from django.http import HttpResponse

from .models import Measurement

# List of all measurements as index page
def index(request):
    measurements = Measurement.objects.all()
    return render(request, "db.html", {"measurements": measurements})

# Add a measurement
def add(request, when, temp, rh):
    measurement = Measurement()
    measurement.when = when
    measurement.temp = temp
    measurement.rh = rh
    measurement.save

    return render(request, "db.html", {"measurements": measurements})
