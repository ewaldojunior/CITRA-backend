# Generated by Django 4.0.4 on 2022-06-15 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CITRApp', '0016_alter_vacancy_shifts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]