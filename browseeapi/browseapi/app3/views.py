from django.shortcuts import render

# Create your views here.


#now we will create a browsable api with some modification of the CRUD operation we did with the last project

from rest_framework.decorators import api_view
from rest_framework.response import Response                                   #This is the Response which we get in the function based api_view
from app3.models import Student
from app3.serializers import StudentSerializer
#giving the status commment
from rest_framework import status



@api_view(['GET','POST', 'PUT','PATCH','DELETE'])                 #This is the CRUD operation within one f(x)
def fc(request, pk =None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

#here we are performing the POST method

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message BOT':'The data is created/POSTED'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#here we will perform the update/PUT method

    if request.method =='PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message':'The data is Complete updated =======================>'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Now this is the request for the partial update
    if request.method =='PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message':'Partial Data Update///////////////////////////>>>>>'})
        return Response(serializer.errors)

#Now we will work on the delete operation
    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'Message Bot':' Data has been Deleted!!==========================>'})