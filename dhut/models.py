from django.db import models

# Create your models here.
class Measurement(models.Model):
    when   = models.DateTimeField("date created")
    temp   = models.FloatField("Temperature in Celsius")
    rh     = models.FloatField("Relative humidity in %")
    sensor = models.IntegerField("Identification of sensor", default=0)

    def as_json(self):
        measurementdict = dict(
                when = self.when,
                temp = self.temp,
                rh = self.rh,
                sensor = self.sensor)
        return measurementdict
