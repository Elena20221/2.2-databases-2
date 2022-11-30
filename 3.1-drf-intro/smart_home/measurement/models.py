import datetime


from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Датчик')
    description = models.CharField(max_length=80, verbose_name='Описание')

    class Meta:
        ordering = ['-id']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата')

    class Meta:
        ordering = ['-created_at']