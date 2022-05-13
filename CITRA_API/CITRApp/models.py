from django.db import models
from uuid import uuid4

class Usuario(models.Model):
    UserId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    NomeCompleto = models.CharField(max_length=255)
    Email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    Senha = models.CharField(max_length=30)
    CPF = models.CharField(max_length=11, unique=True)
    DataNasc = models.DateField(null=True)
    Foto = models.ImageField(null=True)
    Curriculo = models.FileField(null=True)


