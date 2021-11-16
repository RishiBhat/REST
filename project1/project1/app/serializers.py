from rest_framework import serializers



class HumanSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    email =serializers.EmailField(max_length=50)
    state =serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=200)
    msg = serializers.CharField(max_length=200)

  #  def create (self, validated_data):
   #     return Human.objects.create(validated_data)

 #   def update (self, instance, validated_data):
    #    instance.title = validated_data.get('name',instance.name)
     #   instance.title = validated_data.get('email',instance.email)
      #  instance.title = validated_data.get('state',instance.state)
       # instance.title = validated_data.get('city',instance.city)
        #instance.title = validated_data.get('msg',instance.name)