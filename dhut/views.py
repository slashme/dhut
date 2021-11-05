from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import Measurement

# Add a measurement
def add(request):
    measurement = Measurement()
    measurement.when   = request.GET['when']
    measurement.temp   = request.GET['temp']
    measurement.rh     = request.GET['rh']
    measurement.sensor = request.GET['sensor']
    measurement.save()

    return HttpResponse('')

# Landing page
def index(request):
    temps = []
    rhs   = []

    queryset = Measurement.objects.filter(sensor=0,when__gte=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=1))).order_by('when')
    for measurement in queryset:
        temps.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.temp})
        rhs.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.rh})

    measurements = Measurement.objects.filter(sensor=0).order_by('-when')[:20]
    return render(request, 'index.html', {
        'temps'       : temps,
        'rhs'         : rhs,
        "measurements": measurements})

# List of measurements in table form
def db(request):
    measurements = Measurement.objects.filter(sensor=0).order_by('-when')[:200]
    return render(request, "db.html", {"measurements": measurements})

def db1(request):
    measurements = Measurement.objects.filter(sensor=1).order_by('-when')[:200]
    return render(request, "db.html", {"measurements": measurements})

def db2(request):
    measurements = Measurement.objects.filter(sensor=2).order_by('-when')[:200]
    return render(request, "db.html", {"measurements": measurements})

def db3(request):
    measurements = Measurement.objects.filter(sensor=3).order_by('-when')[:200]
    return render(request, "db.html", {"measurements": measurements})

def line_chart(request):
    temps = []
    rhs   = []

    queryset = Measurement.objects.filter(sensor=0,when__gte=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3))).order_by('when')
    for measurement in queryset:
        temps.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.temp})
        rhs.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.rh})

    return render(request, 'line_chart.html', {
        'temps': temps,
        'rhs'  : rhs,
    })

def line_chart1(request):
    temps = []
    rhs   = []

    queryset = Measurement.objects.filter(sensor=1,when__gte=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3))).order_by('when')
    for measurement in queryset:
        temps.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.temp})
        rhs.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.rh})

    return render(request, 'line_chart.html', {
        'temps': temps,
        'rhs'  : rhs,
    })

def line_chart2(request):
    temps = []
    rhs   = []

    queryset = Measurement.objects.filter(sensor=2,when__gte=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3))).order_by('when')
    for measurement in queryset:
        temps.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.temp})
        rhs.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.rh})

    return render(request, 'line_chart.html', {
        'temps': temps,
        'rhs'  : rhs,
    })

def line_chart3(request):
    temps = []
    rhs   = []

    queryset = Measurement.objects.filter(sensor=3,when__gte=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3))).order_by('when')
    for measurement in queryset:
        temps.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.temp})
        rhs.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.rh})

    return render(request, 'line_chart.html', {
        'temps': temps,
        'rhs'  : rhs,
    })
