from rest_framework import serializers

from app11.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields = ['id','name','roll','city']
        