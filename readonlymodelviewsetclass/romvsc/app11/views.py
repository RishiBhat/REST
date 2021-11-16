
from app11.models import Student
from app11.serializers import StudentSerializer
from rest_framework import viewsets

#modelSetView in CRUD operation

class StudentROMVSC(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
