from django.db import models
from django.db.models.fields import related

# Create your models here.

class Teacher(models.Model):
    tname = models.CharField(max_length=50, default="")
    tnumber = models.IntegerField(default=0)                   #One teacher can have multiple students
    remark = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.tname

class Student(models.Model):
    name = models.CharField(max_length=40, default='')
    roll = models.IntegerField(default=0)
    city = models.CharField(max_length=40, default='')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='student', default='')
   
    def __str__(self):
        return self.name



    
  

