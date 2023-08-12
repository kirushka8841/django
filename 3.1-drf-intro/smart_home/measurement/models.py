from django.db import models


class Sensor(models.Model):
    name = models.CharField()
    description = models.CharField()


class Measurement(models.Model):    
    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    created_at = models.DateTimeField(auto_now_add=True)
    