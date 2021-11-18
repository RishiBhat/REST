from django.shortcuts import render

# Create your views here.
from app36.models import Student
from app36.serializers import StudentSerializer
from rest_framework.generics import ListAPIView



class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  