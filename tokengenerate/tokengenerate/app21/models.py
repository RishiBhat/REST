from django.db import models

# Create your models here.


class Student(models.Model):
    name =  models.CharField(max_length=50)
    roll =  models.IntegerField()
    city =  models.CharField(max_length=20)


    def __str__(self):
        return self.name

    #now we will take up the api signals..............

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

#This signa; creates auth tokens for users

@receiver(post_save, sender=settings.AUTH_USER_MODEL)          #register the reciever here......
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
