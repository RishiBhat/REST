from rest_framework import serializers


#we will perform the modelSerializer


from app2.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        

