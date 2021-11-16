#now we will write up the concrete view classes 


from rest_framework.mixins import RetrieveModelMixin
from app8.models import Student
from app8.serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#list and create does not require the pk
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#list, get and retrive and delete the data, require the [pk], all 3 features are available now
class StudentupdateDestroyRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer