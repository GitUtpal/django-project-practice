# Generated by Django 4.0.1 on 2022-01-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelForms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
