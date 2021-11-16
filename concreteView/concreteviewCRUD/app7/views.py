#now we will write up the concrete view classes 


from rest_framework.mixins import RetrieveModelMixin
from app7.models import Student
from app7.serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView



#here we get all the Concrete class
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#Now we will create the data, also the pk required
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#Now we will Retrieve the data, also the pk required in url
class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#Now we will update the data, pk required in url
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#Now we will delete the data, pk required
class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#now we will perform the combined class
#list and create does not require the pk
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#list and get and retrive the data, require the [pk
class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#Retrive and delete the data, require the [pk]
class StudentRetrieveUpdateDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#list, get and retrive and delete the data, require the [pk], all 3 features are available now
class StudentupdateDestroyRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer