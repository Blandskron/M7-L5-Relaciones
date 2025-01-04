from django.db import models

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)

class Curriculum(models.Model):
    trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE)
    documento = models.TextField()
