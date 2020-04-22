from django.db import models

# Create your models here.

class Feedback (models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    description=models.TextField()


class Data(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    Month=models.TextField()
    numberOfDengue=models.IntegerField()
    MOHoffice=models.TextField()
