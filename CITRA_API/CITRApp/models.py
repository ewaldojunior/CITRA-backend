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

    SHIFTS = (
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('I', 'Integral')
    )

    HIRES = (
        ('CTD', 'Contrato de Tempo Determinado'),
        ('CTI', 'Contrato de Tempo Indeterminado'),
        ('CTE', 'Contrato de Trabalho Eventual'),
        ('CE', 'Contrato de Estágio'),
        ('CExp', 'Contrato de Experiência'),
        ('CT', 'Contrato de Teletrabalho'),
        ('CI', 'Contrato Intermitente'),
        ('CTA', 'Contrato de Trabalho Autonômo')
    )

    vacancyId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nameVacancy = models.CharField(max_length=255, blank=False)
    nameCompany = models.CharField(max_length=255, blank=False)
    shifts = models.CharField(max_length=1, choices=SHIFTS, blank=False)
    fone = models.CharField(max_length=13, blank=True)
    cep = models.CharField(max_length=9, blank=False)
    salary = models.FloatField(max_length=25, blank=False)
    picture = models.ImageField(blank=True)
    typeHires = models.CharField(max_length=10, choices=HIRES, blank=True)
    description = models.CharField(blank=True, max_length=500)
    userIdVacancy = models.ForeignKey(User, related_name='userIdVacancy', on_delete=models.CASCADE, default=uuid4)


class Candidacies(models.Model):
     candidaturaId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
     vacancyID = models.ForeignKey(Vacancy, related_name='vacancyID', on_delete=models.CASCADE)
     userID = models.ForeignKey(User, related_name='userID', on_delete=models.CASCADE)