from django.db import models

# Create your models here.
class Project(models.Model):
    startDate=models.DateField(null=True, blank=True)
    endDate=models.DateField(null=True, blank=True)
    name=models.CharField(max_length=30)
    assignedTo=models.CharField(max_length=20)
    priority=models.IntegerField()
