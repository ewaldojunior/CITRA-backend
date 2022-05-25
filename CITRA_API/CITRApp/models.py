from django.db import models
from uuid import uuid4

class User(models.Model):
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

class Vacancy(models.Model):
    vacancyId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nameVacancy = models.CharField(max_length=255)
    nameCompany = models.CharField(max_length=255)
    shifts = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14, unique=True)
    cep = models.CharField(max_length=9, default=0)
    salary = models.FloatField(max_length=25)
    picture = models.ImageField(blank=True)
    typeRemuneration = models.CharField(max_length=100)

class Candidacies(models.Model):
    candidaturaId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    vacancyID = models.ForeignKey(Vacancy, related_name='vacancyID', on_delete=models.CASCADE)
    userID = models.ForeignKey(User, related_name='userID', on_delete=models.CASCADE)
