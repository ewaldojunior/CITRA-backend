# Generated by Django 4.0.4 on 2022-05-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITRApp', '0002_usuario_datanasc_usuario_nomefoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='NomeFoto',
        ),
        migrations.AddField(
            model_name='usuario',
            name='Foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
