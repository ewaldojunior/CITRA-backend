# Generated by Django 4.0.4 on 2022-06-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITRApp', '0015_remove_vacancy_cpf_vacancy_description_vacancy_fone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='shifts',
            field=models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('I', 'Integral')], max_length=1),
        ),
    ]