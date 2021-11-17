

# Create your views here.
from app21.models import Student
from app21.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class fc(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_classes = StudentSerializer
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    