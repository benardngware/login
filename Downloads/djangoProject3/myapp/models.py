from django.db import models

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        self.firstname+' '+self.lastname