from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id' , 'name' , 'roll' , 'city')
    

    #creating all of the  validations
    #Field_value validation 
    def validate_roll(self, value):
        if value>= 200:
            raise serializers.ValidationError('===========================================>', 'School Seat is Full')
        return value

#creating all of the  validations
#Field_value validation 



#object level validation
#def validate(self, data):
 #   nm = data.get('name')
  #  ct = data.get('city')
  #  if nm.lower() == 'rishi' and ct.lower() != 'jammu':
   #     raise serializers.ValidationError('City must be jammu')
   # return data

