# Generated by Django 4.0.4 on 2022-06-18 15:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CITRApp', '0019_remove_vacancy_typeremuneration_vacancy_typehires'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='userIdVacancy',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='userIdVacancy', to='CITRApp.user'),
        ),
    ]