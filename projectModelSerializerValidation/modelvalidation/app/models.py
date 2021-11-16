from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=500)
    roll = models.IntegerField()
    city = models.CharField(max_length=500)

    def __str__(self):
        return self.name

        