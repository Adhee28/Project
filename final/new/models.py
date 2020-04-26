from django.forms import ModelForm
from django.db import models

# Create your models here.

class Feedback2 (models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    description=models.TextField()

    class Meta:
        db_table="feedback"


class DataModel (models.Model):

    Name=models.CharField(max_length=100)
    Year=models.CharField(max_length=100)
    Month=models.CharField(max_length=100)
    NumberOfDengueCase=models.CharField(max_length=100)
    MOHOffice=models.CharField(max_length=100)

    class Meta:
        db_table="dataform"

