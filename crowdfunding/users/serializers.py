from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta: #what Meta class does? a django pattern > meta data > configuration options for data
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}} #'write_only' > only send passwords in, do not allow passwords to be sent out (security). Send user details don't send the password. serilaizer takes DB takes in changescall python function fn(var1,var2) > kwargs are key word arguments > key word and a value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data) #when data comes in > serializer is accessing Custom user model and creating a user. Create user > via default, serializer will send your values to DB (password, username) > serializer will send out of the box. We want passwords to be saved as a HASH > HASH masks the password. create_user > special function in Django that will HASH passwords. Create the CREATE function to over-write the default behaviour.