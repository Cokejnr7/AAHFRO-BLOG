from rest_framework import authentication,exceptions
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings


User = get_user_model()

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        auth_data = authentication.get_authorization_header(request)
        
        if not auth_data:
            return
        
        prefix,token= auth_data.decode('utf-8').split(" ")
        
        try:
            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"])
            user  = User.objects.get(username=payload["username"])
            
            return (user,token)
        
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                f"Invalid token {identifier}")

        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("your token is expired") 
        
        
        
        return super.authenticate(request)
        