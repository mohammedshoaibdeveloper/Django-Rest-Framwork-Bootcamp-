from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
# Create your views here.






@api_view(['GET','POST'])
def index(request):

    if request.method == 'GET':
        return Response({'status':200,'messge':"get call"})


    if request.method == 'POST':
        return Response({'status':200,'messge':"post call"})






@api_view(['GET'])
def get_student(request):

    data = Student.objects.all().order_by('-id')
    serializer = StudentSerializer(data,many=True)
    return Response({'status':200,'messge':"Get data",'data':serializer.data})


@api_view(['POST'])
def add_student(request):

    serialzer = StudentSerializer(data = request.data)
    if not serialzer.is_valid():
        return Response({'status':403,'errors':serialzer.errors,'message':'something went wrong'})

    serialzer.save()

    return Response({'status':201,'messge':"Add data",'data':serialzer.data})

    