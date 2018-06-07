from rest_framework import serializers
from .models import Access_Log,Data_LogA,Data_LogD,Data_LogC,Data_LogB,FeedBack
from django.contrib.auth.models import User

class Access_Log_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Access_Log
        fields=('User','time')

class Data_LogASerializer(serializers.ModelSerializer):
    class Meta:
        model=Data_LogA
        fields=('__all__')

class Data_LogBSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data_LogB
        fields = ('__all__')

class Data_LogCSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data_LogC
        fields = ('__all__')

class Data_LogDSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data_LogD
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
            class Meta:
                model=User
                fields=('__all__')
class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model=FeedBack
        fields=('__all__')