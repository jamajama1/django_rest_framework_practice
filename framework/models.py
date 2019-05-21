from django.db import models

# Create your models here.
class Interns(models.Model):
    name = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=100)
    year = models.CharField(max_length=20)

