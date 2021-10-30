from django.db import models

# Create your models here.
class Measurement(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    temp = models.FloatField("Temperature in Celsius")
    rh   = models.FloatField("Relative humidity in %")
