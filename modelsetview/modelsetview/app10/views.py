
from app10.models import Student
from app10.serializers import StudentSerializer
from rest_framework import viewsets

#modelSetView in CRUD operation

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer