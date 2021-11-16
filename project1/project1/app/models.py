from django.db import models

# Create your models here.


class Portfolio(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=50)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=200)
    msg = models.TextField(max_length=200)

    def __str__(self):
        return self.name

