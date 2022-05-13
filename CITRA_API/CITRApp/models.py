from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class Usuario(models.Model):
    UserId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    NomeCompleto = models.CharField(max_length=255)
    Email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    Senha = models.CharField(max_length=30)
    CPF = models.CharField(max_length=11, unique=True)
    DataNasc = models.DateField(null=True)
    Celular = models.CharField(null=True, max_length=11)
    Foto = models.ImageField(null=True)
    Curriculo = models.FileField(null=True)

    def __str__(self):
        return self.NomeCompleto


