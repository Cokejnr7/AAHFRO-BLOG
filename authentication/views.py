from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.conf import settings
from .serializers import UserSerilizer
import jwt


# Create your views here.
class LoginView(generics.GenericAPIView):
    
    def post(self,request):
        data = request.data
        
        username = data.get('username','')
        password = data.get('password','')
        
        user = authenticate(username=username,password=password)
        
        if user:
            token = jwt.encode({"username":user.username},settings.SECRET_KEY,algorithm='HS256')
            
            serializer = UserSerilizer(user)
            
            data = {"user":serializer.data,"token":token}
            
            return Response(data,status=status.HTTP_200_OK)
        
        return Response({"message": "invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
        
        