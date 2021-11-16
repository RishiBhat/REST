from rest_framework import serializers

from .models import  Rishi



class RishiSerializers(serializers.Serializer):
    class Meta:
        model = Rishi
        fields = ('id' , 'employee_id' , 'job_title' , 'company')
employee_id=serializers.IntegerField()
job_title=serializers.CharField(max_length=50)
company=serializers.CharField(max_length=20)
        