



from rest_framework.decorators import permission_classes
from app13.models import Student
from app13.serializers import StudentSerialzer
from rest_framework import viewsets 
from rest_framework.authentication import SessionAuthentication   
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissions
#modelSetView in CRUD operation

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]
    
    #permission_classes =[IsAuthenticatedOrReadOnly]             #if registered, read update and delete

    #permission_classes = [IsAdminUser]                                    #This is only when the staff check boxes are ticked 
    
    #This is for any type of user
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated]

#This is gives us the basic API


#To take up the built in login using it from the url