

# Create your views here.
from app24.models import Student
from app24.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class fc(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer                          #The serializer attribute should be same as that of the serializers.py class, otherwise error of missing attribute
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

