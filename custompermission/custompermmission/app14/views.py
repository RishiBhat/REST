from rest_framework.decorators import permission_classes
from app14.models import Student
from app14.serializers import StudentSerialzer
from rest_framework import viewsets 
from rest_framework.authentication import SessionAuthentication   
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from app14.custompermissions import MyPermission


class StudentModelViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    #here we will write up a custom class
    
    permission_classes = [MyPermission] #this is the custom permission which we wrote in permissions.py file

    


