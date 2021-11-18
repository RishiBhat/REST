from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20, default ='')
    roll = models.IntegerField(default=10)
    city = models.CharField(max_length=10, default ='')
    invigilator = models.CharField(max_length=20, blank=True, null= True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs): 
        self.invigilator = 'rishi'
        super(Student, self).save(*args, **kwargs)
     