


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response                                   #This is the Response which we get in the function based api_view
from app15.models import Student
from app15.serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(['GET','POST', 'PUT', 'DELETE'])                 #This is the CRUD operation within one f(x)
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])

def fc(request):
    if request.method == 'GET':
        id = request.data.get('id')
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
            return Response({'message BOT':'The data is created/POSTED'})
        return Response(serializer.errors)


#here we will perform the update/PUT method

    if request.method =='PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message':'The data is update=======================>'})
        return Response(serializer.errors)


#Now we will work on the delete operation
    if request.method == 'DELETE':
        id =request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'Message Bot':' Data has been Deleted!!==========================>'})