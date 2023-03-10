from django.shortcuts import render,HttpResponse
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

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentView(APIView):

    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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

from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistration(APIView):

    def post(self,request):

        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

        serializer.save()
        user = User.objects.get(username = serializer.data['username'])

        refresh = RefreshToken.for_user(user)
        print("------------------------",refresh)
        return HttpResponse("ok")
        # token_obj , _ = Token.objects.get_or_create(user=user)


        return Response({'status':200,
        'data':serializer.data,
        'token_obj':str(refresh),
        'access':str(refresh.access_token),
        'message':'your data is saved'})

        # return Response({'status':200,'data':serializer.data,'token_obj':str(token_obj),'message':'your data is saved'})



class Register(APIView):

    def post(self, request):
        serializer = CustomeUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})

        serializer.save()
        return Response({'status':200,'message':'Account Created Successfully'})

