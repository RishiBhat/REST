
from rest_framework import serializers
from .models import Portfolio




class PortSerializer(serializers.ModelSerializer):
    #name =  serializers.CharField(read_only=True)
    class Meta:
        model = Portfolio
        fields = '__all__'
        read_only_fields = ['id']
        #one more way to update the fields is to use the kwargs keywords
        kwargs = {'name':{'read_only': True}}
        

    def validate_roll(self,value):
        if value>250:
            raise serializers.ValidationError('Correct it!!')
        return value

        