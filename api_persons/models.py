from django.db import models

# Create your models here.
class Person(models.Model):
    TipoDocumento=models.CharField(max_length=50)
    Documento=models.CharField(max_length=500)
    Nombres=models.CharField(max_length=500)
    Apellidos=models.CharField(max_length=500)
    Hobbie=models.CharField(max_length=500)