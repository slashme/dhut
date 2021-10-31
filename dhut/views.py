from django.shortcuts import render
from django.http import HttpResponse
import datetime

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

def line_chart(request):
    temps = []
    rhs   = []

    queryset = Measurement.objects.all().order_by('-id')[:2000]
    epoch=datetime.datetime(2021,10,30)
    for measurement in queryset:
        temps.append({'x': (measurement.when.replace(tzinfo=None) - epoch).total_seconds(), 'y': measurement.temp})
        rhs.append({'x': (measurement.when.replace(tzinfo=None) - epoch).total_seconds(), 'y': measurement.rh})

    return render(request, 'line_chart.html', {
        'temps': temps,
        'rhs'  : rhs,
    })
