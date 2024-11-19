from rest_framework import permissions
from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from jwt.exceptions import ExpiredSignatureError, DecodeError
from fastapi import Request, HTTPException, status
# from jose import jwt, ExpiredSignatureError, JWTError
from asgiref.sync import sync_to_async  
from decouple import config
from Api.models import *
from Api.models import *
import jwt


##Only for admin

class authorization(permissions.BasePermission):

    def has_permission(self, request, view):
        try:

           
            token_catch = request.META['HTTP_AUTHORIZATION'][7:]
            request.GET._mutable = True
            my_token = jwt.decode(token_catch,config('USERJWTTOKEN'),algorithms=["HS256"])
            request.GET['token'] = my_token
            UserToken.objects.get(user = my_token['id'],token = token_catch)
            request.auth = my_token
            return True
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed({"status": False,"error":"Session Expired !!"})
        except jwt.DecodeError:
            raise AuthenticationFailed({"status": False,"error":"Invalid token"})
        except Exception as e:
            raise AuthenticationFailed({"status": False,"error":"Need Login", "e": e})



class UserPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            auth_token = request.META["HTTP_AUTHORIZATION"][7:]
            decode_token = jwt.decode(auth_token, config('USERJWTTOKEN'), "HS256")
            whitelist = UserToken.objects.filter(user =  decode_token['id'],token = auth_token).exists()
            if not whitelist:
                # raise AuthenticationFailed("You must need to Login first")
                raise NeedLogin()
            request.auth = decode_token
            return True
        except AuthenticationFailed as af:
            raise NeedLogin()
        except jwt.ExpiredSignatureError:
            raise NeedLogin()
            # raise AuthenticationFailed({"status": False,"error":"Session Expired !!"})
        except jwt.DecodeError:
            raise NeedLogin()
            # raise AuthenticationFailed({"status": False,"error":"Invalid token"})
        except Exception as e:
            raise NeedLogin()
            # raise AuthenticationFailed({"status": False,"error":"Need Login"})


# Custom Exception for Authentication Failures
class NeedLogin(HTTPException):
    def __init__(self, detail: str = "You must need to login first"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )

# FastAPI Dependency for Authentication
async def get_current_user(request: Request):
    try:
        # Get Authorization header from the request
        auth_header = request.headers.get("Authorization")
        if auth_header is None or not auth_header.startswith("Bearer "):
            raise NeedLogin("Authorization header is missing or improperly formatted.")

        # Extract JWT token from Authorization header
        auth_token = auth_header[7:]
        
        # Decode the JWT token
        decode_token = jwt.decode(auth_token, config('USERJWTTOKEN'), algorithms=["HS256"])

        # Check if the token is whitelisted in the database
        whitelist = await sync_to_async(UserToken.objects.filter(user=decode_token['id'], token=auth_token).exists)()

        if not whitelist:
            raise NeedLogin("Token not whitelisted or invalid.")

        return decode_token
    except ExpiredSignatureError:
        raise NeedLogin("JWT token has expired.")
    except JWTError:  # Use a broader JWTError exception to catch decoding issues
        raise NeedLogin("JWT token is invalid.")
    except Exception as e:
        raise NeedLogin(f"An unexpected error occurred: {str(e)}")

# class AdminPermission(BasePermission):
#     def has_permission(self, request, view):
#         try:
#             auth_token = request.META["HTTP_AUTHORIZATION"][7:]
#             decode_token = jwt.decode(auth_token, config('ADMINJWTTOKEN'), "HS256")
#             whitelist = AdminWhitelistToken.objects.filter(admin =  decode_token['id'],token = auth_token).exists()
#             if not whitelist:
#                 raise AuthenticationFailed("You must need to Login first")
#             request.auth = decode_token
#             return True
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed({"status": False,"error":"Session Expired !!"})
#         except jwt.DecodeError:
#             raise AuthenticationFailed({"status": False,"error":"Invalid token"})
#         except Exception as e:
#             raise AuthenticationFailed({"status": False,"error":"Need Login"})






class NeedLogin(APIException):
    status_code = 401
    default_detail = {'status': False, 'message': 'Unauthorized'}
    default_code = 'not_authenticated'