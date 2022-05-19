from django.db import models
from uuid import uuid4

class Usuario(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    birthdate = models.DateField()
    fone = models.CharField(max_length=13, default=0)
    picture = models.ImageField(blank=True)
    cv = models.FileField(blank=True)
    cep = models.CharField(max_length=9, default=0)
    description = models.CharField(null=True, max_length=500)

    def __str__(self):
        return self.name


