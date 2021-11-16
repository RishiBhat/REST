from rest_framework import serializers

from app13.models import Student

class StudentSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
