
from django.contrib.admin.options import IS_POPUP_VAR
from app18.models import Student
from app18.serializers import StudentSerializer
from rest_framework import viewsets 
from rest_framework.authentication import TokenAuthentication   
from rest_framework.permissions import IsAuthenticated

#This is the token authentication

class StudentModelViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    #This is for any type of user
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

#This is gives us the basic API
