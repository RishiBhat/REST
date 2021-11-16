

from rest_framework.response import Response
from app9.models import Student
from app9.serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    #It will get us all the items
    def list(self, request):
        print("**************List***************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name:", self.name)
        print("Description", self.description)
        obj = Student.objects.all()
        isserialized = StudentSerializer(obj, many=True)
        return Response(isserialized.data)  

    #now we ill perform the retrieve, gives us the single record, get single obj
    def retrieve(self, request, pk =None):

        #checking and learning about the attributes over here

        print("*************Retrieve***************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name:", self.name)
        print("Description", self.description)
        
        id = pk
        if id is not None:    
            obj = Student.objects.get(id=id)
            isserialized = StudentSerializer(obj)
            return Response(isserialized.data)
    #now we will perform the create 

    def create(self, request, pk=None):
        print("*************Create***************")

        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name:", self.name)
        print("Description", self.description)
        
        isserialized = StudentSerializer(data=request.data)
        if isserialized.is_valid():
            isserialized.save()
            return Response({'BOT':'Data is created now'}, status = status.HTTP_201_CREATED)
        return Response(isserialized.errors, status=status.HTTP_400_BAD_REQUEST)

    #now we will perofmr the update
    def update(self, request, pk):
        print("*************Update***************")

        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name:", self.name)
        print("Description", self.description)
        
        id = pk
        obj = Student.objects.get(pk = id) 
        isserialized = StudentSerializer(obj, data=request.data)
        if isserialized.is_valid():
            isserialized.save()
            return Response({'BOT':"Data is updated now"})
        return Response(isserialized.errors, status =status.HTTP_400_BAD_REQUEST)
    #now we ill update partial 

    def partial_update(self, request, pk):
        print("*************Partial Update***************")

        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name:", self.name)
        print("Description", self.description)
        
        id=pk
        obj = Student.objects.get(pk=id)
        isserialized = StudentSerializer(obj, data=request.data, partial=True)
        if isserialized.is_valid():
            isserialized.save()
            return Response({'BOT':"Partial Data Update"})
        return Response(isserialized.errors)

    #now we willl perform the destroy
    
    def delete(self, request, pk):
        print("*************Destroy***************")
        print("Basename", self.basename)
        print("Action", self.action)
        print("Detail", self.detail)
        print("Suffix", self.suffix)
        print("Name:", self.name)
        print("Description", self.description)
        
        id = pk
        obj = Student.objects.get(pk=id)
        obj.delete()
        return Response({'BOT': "Data is deleted now"})


