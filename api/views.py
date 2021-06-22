from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response


@api_view(['POST'])
def UsersCreate(request):
    serializer = User_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        serv = request.data['service']
        loca = request.data['location']
        print(serv)
        print(loca)
        serv = serv.lower()
        queryset = ServiceProvider.objects.filter(location=loca, service=serv)
        result = ProfileSerialiser(queryset, many=True)
        return Response(result.data)
    else:
        return Response("An error occured")


@api_view(['POST', 'GET'])
def UsersList(request):
    users = Client.objects.all().order_by('-id')
    serializer = User_Serializer(users, many=True)
    return Response(serializer.data)
