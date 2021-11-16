
from rest_framework import serializers


#we will perform the browsable api 


from app3.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        


