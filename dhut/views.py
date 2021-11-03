from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import Measurement


# Landing page
def index(request):
    temps = []
    rhs   = []

    queryset = Measurement.objects.filter(when__gte=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=1))).order_by('when')
    for measurement in queryset:
        temps.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.temp})
        rhs.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.rh})

    measurements = Measurement.objects.all().order_by('-when')[:20]
    return render(request, 'index.html', {
        'temps'       : temps,
        'rhs'         : rhs,
        "measurements": measurements})

# List of all measurements as index page
def db(request):
    measurements = Measurement.objects.all().order_by('-when')[:200]
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

    queryset = Measurement.objects.filter(when__gte=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=3))).order_by('when')
    for measurement in queryset:
        temps.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.temp})
        rhs.append({'x': str(measurement.when).replace(" ","T"), 'y': measurement.rh})

    return render(request, 'line_chart.html', {
        'temps': temps,
        'rhs'  : rhs,
    })
