# Generated by Django 4.0.4 on 2022-06-14 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITRApp', '0014_rename_usuario_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='cpf',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='fone',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]