from django.db import models


class Car(models.Model):
  id = models.AutoField(primary_key = true)
  model = models.models.CharField(max_lenght = 200)
  brand = models.CharField(max_length = 200)
  factory_year = models.IntegerField(blank=true, null = True)
  model_year = models.IntegerField(blank=true, null = True)
  value = models.FloatField(blank=true, null = True)




