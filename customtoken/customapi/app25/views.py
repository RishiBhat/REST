from django.contrib.admin.options import IS_POPUP_VAR
from app25.models import Student
from app25.serializers import StudentSerializer
from rest_framework import viewsets 
from rest_framework.authentication import TokenAuthentication   
from rest_framework.permissions import IsAuthenticated
from app25.customauth import CustomAuth
#This is the token authentication

class fc(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuth]
    permission_classes = [IsAuthenticated]
