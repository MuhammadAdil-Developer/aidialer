from decouple import config
import jwt, datetime
from Api.models import *
from Api.models import *
from django.conf import settings

def UserGenerateToken(fetchuser: User):
    try:
        secret_key = config("USERJWTTOKEN")
        # Set the token to expire in 2 minutes
        token_payload = {
            "id": str(fetchuser.id),
            "email": fetchuser.email,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),  # Token will expire in 2 minutes
        }
        detail_payload = {
            "id": str(fetchuser.id),
            "email": fetchuser.email,
            "Name": fetchuser.name,
        }

        # Generate the token
        token = jwt.encode(token_payload, key=secret_key, algorithm="HS256")

        # Save the token to the database
        UserToken.objects.create(user=fetchuser, token=token)

        return {"status": True, "token": token, "payload": detail_payload}
    
    except Exception as e:
        return {"status": False, "message": f"Error during token generation: {str(e)}"}


def UserDeleteToken(fetchuser, request):
    try:
        token = request.META["HTTP_AUTHORIZATION"][7:]
        whitelist_token = UserToken.objects.filter(user=fetchuser.id, token=token).first()
        if whitelist_token:
            whitelist_token.delete()
        admin_all_tokens = UserToken.objects.filter(user=fetchuser)
        for fetch_token in admin_all_tokens:
            try:
                jwt.decode(fetch_token.token, settings.USERJWTTOKEN, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                fetch_token.delete()
        return True
    except Exception:
        return False




# def admin_generate_token(fetchuser:SuperAdmin):
#     try:
#         secret_key = config("ADMINJWTTOKEN")
#         total_days = 1
#         token_payload = {
#             "id": str(fetchuser.id),
#             "email":fetchuser.email,
#             "iat": datetime.datetime.utcnow(),
#             "exp": datetime.datetime.utcnow() + datetime.timedelta(days=total_days),
#             # "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1),  
              
#         }
#         detail_payload = {
#             "id": str(fetchuser.id),
#             "email":fetchuser.email,
#             "first_name": fetchuser.fname,
#             "last_name": fetchuser.lname,
#             "contact": fetchuser.contact,
#             "profile": fetchuser.profile.url
#         }
#         token = jwt.encode(token_payload, key= secret_key, algorithm="HS256")
#         AdminWhitelistToken.objects.create(admin = fetchuser, token = token)
#         return {"status": True, "token" : token, "payload": detail_payload}
#     except Exception as e:
#         return {"status": False, "message": f"Error during generationg token {str(e)}"}



# def admin_delete_token(fetchuser, request):
#     try:
#         token = request.META["HTTP_AUTHORIZATION"][7:]
#         whitelist_token = AdminWhitelistToken.objects.filter(admin = fetchuser.id, token = token).first()
#         whitelist_token.delete()
#         admin_all_tokens = AdminWhitelistToken.objects.filter(admin = fetchuser)
#         for fetch_token in admin_all_tokens:
#             try:
#                 decode_token = jwt.decode(fetch_token.token, config('ADMINJWTTOKEN'), "HS256")
#             except:    
#                 fetch_token.delete()
#         return True
#     except Exception :
#         return False
