from rest_framework import serializers



# here we need to explicitly define our object id otherwise it will not render the elements


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=200)
    city=serializers.CharField(max_length=10)
    msg=serializers.CharField(max_length=500)    





# here we are perform the desrializtion with another Portfolio class by using the def create function with serializers.validated_data()
# this creates the model objects in our db, aslo the deserilization is performed with the help of serializers class...

from rest_framework import serializers

class Portfolio(serializers.Serializer):
    pname=serializers.CharField(max_length=200)
    pcity=serializers.CharField(max_length=20)
    pstate=serializers.CharField(max_length=25)

    def create(self,validated_data):
        return Portfolio.objects.create(**validate_data)