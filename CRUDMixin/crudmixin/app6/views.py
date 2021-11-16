
from app6.models import Student
from app6.serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


#creating a f(x) and class to GET the all class
#now we will create the two groups into list and create [pk], NA

class ListCreateAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
#now we will write up a class and POST
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#Retrieve update and Destroy - Pk Required
class RUDStudentApi(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

