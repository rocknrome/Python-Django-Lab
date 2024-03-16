from django.db import models

# Create your models here.

## Create New Model Class that Inherits from models.Model
class Turtle(models.Model):
    # Define the fields in the model
    # Define a string field of 100 char max
    name = models.CharField(max_length=100)
    # define a age that is an integer (whole number)
    age = models.IntegerField()

class Dog(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()

class Cat(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()

class Bird(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()