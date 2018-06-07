from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Access_Log,Data_LogA,Data_LogB,Data_LogC,Data_LogD,FeedBack
from django.contrib.auth.models import User
from .serializer import Access_Log_Serializer,UserSerializer,Data_LogASerializer,Data_LogBSerializer,Data_LogCSerializer,Data_LogDSerializer,FeedBackSerializer

class Access_LogList(APIView):
    def get(self,request):
        access=Access_Log.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Access_Log_Serializer(access,many=True)
        return Response(serializer.data)
    def post(self,request):
       pass

# Create your views here.
class UserList(APIView):
    def get(self,request):
        user=User.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            u = User.objects.create(username=data['username'])
            u.set_password(data['password'])
            u.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Data_LogAList(APIView):
    def get(self,request):
        data_log=Data_LogA.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Data_LogASerializer(data_log,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Data_LogASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Data_LogBList(APIView):
    def get(self,request):
        data_log=Data_LogB.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Data_LogBSerializer(data_log,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Data_LogBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Data_LogCList(APIView):
    def get(self,request):
        data_log=Data_LogC.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Data_LogCSerializer(data_log,many=True)
        return Response(serializer.data)
    def post(self,request):
        serialzer=Data_LogCSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data,status=status.HTTP_201_CREATED)
        return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)

class Data_LogDList(APIView):
    def get(self,request):
        data_log=Data_LogD.objects.all()
        # many tells us that there are many objects to serialize
        # serializer is used to convert our models to json data which is basically a string
        serializer=Data_LogDSerializer(data_log,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Data_LogDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class FeedBackList(APIView):
    def get(self,request):
        f=FeedBack.objects.all()
        serializer=FeedBackSerializer(f,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)