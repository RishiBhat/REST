from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from app40.models import Student, Teacher
from app40.serializers import StudentSerializer, TeacherSerializer
from rest_framework import viewsets


class student(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class Teacher(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


