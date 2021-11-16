from rest_framework import serializers

from app14.models import Student

class StudentSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']