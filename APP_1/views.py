from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from APP_1.models import Student
from APP_1.serializer import StudentSerializer


# Create your views here.
@api_view(['POST'])
def save(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#ngrok

@ api_view(['GET'])
def fetch(request):
    Student.objects.create(names="Tara Maria",email="tara@gmail.com",password='123456',gender="Male",sports="soccer",education="College",)
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)