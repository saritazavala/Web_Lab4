from django.db import models

# Create your models here.

class Parent(models.Model):
    name = models.CharField(max_length=20,null=True)
    lastName = models.CharField(max_length=20,null = True)
    user = models.CharField(max_length=20,null=True)


