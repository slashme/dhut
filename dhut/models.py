from django.db import models

# Create your models here.
class Measurement(models.Model):
    when = models.DateTimeField("date created")
    temp = models.FloatField("Temperature in Celsius")
    rh   = models.FloatField("Relative humidity in %")
