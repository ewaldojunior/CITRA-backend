# Generated by Django 4.0.4 on 2022-05-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITRApp', '0004_usuario_curriculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Telefone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
