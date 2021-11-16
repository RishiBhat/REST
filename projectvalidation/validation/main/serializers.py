from rest_framework import serializers, validators
from rest_framework.exceptions import ValidationError
from .models import Emp 


#validators
def start_with_r(value): 
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with r')
    return value

class EmpSerializers(serializers.Serializer):


    name=serializers.CharField(max_length=20, validators=[start_with_r])
    email=serializers.CharField(max_length=50)
    phone=serializers.IntegerField()

    def create(self,validate_data):
        return Emp.objects.create(**validate_data)
    
#Now we are performing field level validation
#Its just performed on the single field 

    def validate_phone(self, value):
        if value >=9090909090090:
            raise serializers.ValidationError('Contact Number not valid')
        return value
#We are performing the object level validation with the many fields

    def validate(self, data):
        nm = data.get('name')
        em = data.get('email')
        
        if nm.lower()=='Naruto' and em.lower() != 'l@p.com':
            raise serializers.ValidationError("This is not the correct data")
        return data
    
    #validators
    def start_with_9(value): 
        if value[0].lower() != 9:
            raise serializers.ValidationError('Number should start with 9')

    #def update(self,instance,validate_data): 
     #   instance.phone_number=validate_data.get('phone_number',instance.phone_number) 
      #  instance.name=validate_data.get('name',instance.name)
     ##   instance.email=validate_data.get('email',instance.email)

       ## instance.save()
       ## return instance

#Now we are performing field level validation
#Its just performed on the single field 

   

