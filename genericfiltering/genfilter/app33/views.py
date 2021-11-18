from django.shortcuts import render

# Create your views here.
from app33.models import Student
from app33.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
#Now without the global registration of django-filter we use it as the class wise for that we need to import it here...
from django_filters.rest_framework import DjangoFilterBackend



class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #now we need to configure where exactly we need filter to work,
    filter_backends = [DjangoFilterBackend]    #explicit declaration of the django_filters
    filterset_fields = ['city']      #now how to hit the client