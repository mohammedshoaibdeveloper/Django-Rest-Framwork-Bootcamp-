from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.views import APIView
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


@api_view(['PATCH'])
def patch_student(request,id):

    studentObj = Student.objects.get(id = id)

    serializer = StudentSerializer(studentObj,data = request.data,partial = True)
    if not serializer.is_valid():
        return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

    serializer.save()

    return Response({'status':201,'messge':"Add data",'data':serializer.data})

    

@api_view(['PUT'])
def put_student(request,id):

    studentObj = Student.objects.get(id = id)

    serializer = StudentSerializer(studentObj,data = request.data)
    if not serializer.is_valid():
        return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

    serializer.save()

    return Response({'status':201,'messge':"Add data",'data':serializer.data})


@api_view(['DELETE'])
def delete_student(request,id):

    try:
        studentObj = Student.objects.get(id = id)
        studentObj.delete()

        return Response({'status':201,'messge':"Deleted Successfully"})
    except Exception as e:
        return Response({'status':403,'message':'no data found'})


@api_view(['GET'])
def get_book(request):

    data = Book.objects.all().order_by('-id')
    serializer = BookSerializer(data,many=True)
    return Response({'status':200,'messge':"Get data",'data':serializer.data})



class StudentView(APIView):

    def get(self, request):

        data = Student.objects.all().order_by('-id')
        serializer = StudentSerializer(data,many=True)
        return Response({'status':200,'messge':"Get data",'data':serializer.data})

    def post(self, request):

        serialzer = StudentSerializer(data = request.data)
        if not serialzer.is_valid():
            return Response({'status':403,'errors':serialzer.errors,'message':'something went wrong'})

        serialzer.save()

        return Response({'status':201,'messge':"Add data",'data':serialzer.data})

    def patch(self, request):

        try:

            id = request.data.get('id')
            studentObj = Student.objects.get(id = id)

            serializer = StudentSerializer(studentObj,data = request.data,partial = True)
            if not serializer.is_valid():
                return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

            serializer.save()

            return Response({'status':201,'messge':"Add data",'data':serializer.data})

        except Exception as e:
            return Response({'status':403,'message':'no data found'})


    def put(self, request):
        try:
            id = request.data.get('id')
            studentObj = Student.objects.get(id = id)

            serializer = StudentSerializer(studentObj,data = request.data)
            if not serializer.is_valid():
                return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

            serializer.save()

            return Response({'status':201,'messge':"Add data",'data':serializer.data})
        except Exception as e:
            return Response({'status':403,'message':'no data found'})
    def delete(self, request):

        try:
            id = request.data.get('id')
            studentObj = Student.objects.get(id = id)
            studentObj.delete()

            return Response({'status':201,'messge':"Deleted Successfully"})
        except Exception as e:
            return Response({'status':403,'message':'no data found'})