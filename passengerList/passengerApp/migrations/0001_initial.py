# Generated by Django 4.0.1 on 2022-01-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='passengerList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('emailId', models.CharField(max_length=30)),
                ('rewardPoint', models.CharField(max_length=3)),
            ],
        ),
    ]