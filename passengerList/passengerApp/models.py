from django.db import models

# Create your models here.
class PassengerList(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    emailId=models.CharField(max_length=30)
    rewardPoint=models.CharField(max_length=3)
