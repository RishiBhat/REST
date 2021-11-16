from django.shortcuts import render

# Create your views here.


#now we will create a class based APIView here 

from rest_framework.response import Response                                   #This is the Response which we get in the function based api_view
from app4.models import Student
from app4.serializers import StudentSerializer
#giving the status commment
from rest_framework import status
from rest_framework.views import APIView                                     #This is the APIView which we get after import. 



class StudentAPI(APIView):
    #now only method functions will be made 
    def get(self, request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
       
#here we are performing the POST method

    def post(self, request,pk,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message BOT':'The data is created/POSTED'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#here we will perform the update/PUT method
    def put(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message':'The data is Complete updated =======================>'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Now this is the request for the partial update

    def patch(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message':'Partial Data Update///////////////////////////>>>>>'})
        return Response(serializer.errors)

#Now we will work on the delete operation
    def delete(self, request, pk, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'Message Bot':' Data has been Deleted!!==========================>'})