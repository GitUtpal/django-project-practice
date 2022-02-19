from django.db import models

# Create your models here.
class Movie(models.Model):
    #name releasedate rating
    movieName=models.CharField(max_length=30)
    releaseDate=models.DateField(null=True, blank=True)
    rating=models.IntegerField()
