from re import S
from rest_framework import serializers


from app34.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','roll','city']


        