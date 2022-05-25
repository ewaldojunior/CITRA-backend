# Generated by Django 4.0.4 on 2022-05-24 00:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CITRApp', '0011_alter_usuario_cv_alter_usuario_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('vacancyId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nameVacancy', models.CharField(max_length=255)),
                ('nameCompany', models.CharField(max_length=255)),
                ('shifts', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('cep', models.CharField(default=0, max_length=9)),
                ('salary', models.FloatField(max_length=25)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('typeRemuneration', models.CharField(max_length=100)),
            ],
        ),
    ]
