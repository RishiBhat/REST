#GenericAPIView and Model Mixin will start form here now, they will be taking a value


from app5.models import Student
from app5.serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


#creating a f(x) and class to GET the all class
class StudentList(GenericAPIView, ListModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


#now we will write up a class and POST


class StudentList(GenericAPIView, CreateModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#now we will retrieve the data 

class StudentRetrive(GenericAPIView, RetrieveModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

#now we will perform the update

class StudentUpdate(GenericAPIView, UpdateModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


#now we will delete

class StudentDelete(GenericAPIView, DestroyModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#if we want to take up the all model we need to have the [pk] period.  