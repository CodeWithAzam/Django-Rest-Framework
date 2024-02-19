from rest_framework import serializers
# from blog.models import Task

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ('id', 'username', 'email', 'password')
        extra_kwargs= {'password', {'write_only': True}} 




# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'