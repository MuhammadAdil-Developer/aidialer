from rest_framework import serializers
from passlib.hash import django_pbkdf2_sha256 as handler
from django.contrib.auth.hashers import make_password
from Usable import usable as uc
from .models import *
from .serializer import *
import re

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)  # Optional field for PIN
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


    def validate_email(self, value):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):  # Basic email format validation
            raise serializers.ValidationError("Email Format Is Incorrect")
        return value

    def passwordLengthValidator(self, value):
        if not uc.validate_password(value):
            raise serializers.ValidationError("Password must contain at least one special character and one uppercase letter, and be between 8 and 20 characters long")
        return make_password(value)


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        
        fetch_user = User.objects.filter(email=email).first()
        if not fetch_user:
            raise serializers.ValidationError("Email not found . . .")
        
        check_pass = handler.verify(password, fetch_user.password)
        if not check_pass:
            raise serializers.ValidationError("Wrong Password !!!")
        
        attrs["fetch_user"] = fetch_user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    oldpassword = serializers.CharField(required=True)
    newpassword = serializers.CharField(required=True, min_length=8, max_length=20)

    def validate_newpassword(self, value):
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char in "!@#$%^&*()_+" for char in value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return value

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class OtpTokenSerializer(serializers.Serializer):
    otp = serializers.IntegerField(required=True)
    id = serializers.IntegerField(required=True)

class ResetPasswordSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    newpassword = serializers.CharField(required=True, min_length=8, max_length=20)

    def validate_newpassword(self, value):
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")
        if not any(char in "!@#$%^&*()_+" for char in value):
            raise serializers.ValidationError("Password must contain at least one special character.")
        return value

class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptRecord
        fields = [

            'id','assistance_name','welcome_message','salesperson_name', 'salesperson_role', 'company_name', 'company_business',
            'company_values', 'conversation_purpose', 'conversation_further_information',
            'QNA', 'conversation_type', 'template_type'
        ]

class TwilioInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwilioInfo
        fields = ['twilio_sid', 'twilio_token', 'twilio_number', 'label_name']

class PromptSerializer(serializers.ModelSerializer):
    template_type = serializers.ChoiceField(
        choices=[
            ('appointment-setter', 'Appointment Setter'),
            ('customer-support', 'Customer Support'),
            ('inbound', 'Inbound'),
            ('game-npc', 'Game NPC')
        ]
    )
    assistance_name = serializers.CharField(required=False, allow_blank=True)
    welcome_message = serializers.CharField(required=False, allow_blank=True)
    salesperson_role = serializers.CharField(required=False, allow_blank=True)
    salesperson_name = serializers.CharField(required=False, allow_blank=True)
    company_name = serializers.CharField(required=False, allow_blank=True)
    company_business = serializers.CharField(required=False, allow_blank=True)
    company_values = serializers.CharField(required=False, allow_blank=True)
    conversation_purpose = serializers.CharField(required=False, allow_blank=True)
    conversation_type = serializers.CharField(required=False, allow_blank=True)
    conversation_further_information = serializers.CharField(required=False, allow_blank=True)
    QNA = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = PromptRecord
        fields = (
            'assistance_name','salesperson_name', 'salesperson_role', 'company_name', 'company_business',
            'company_values', 'conversation_purpose', 'conversation_further_information',
            'QNA', 'conversation_type', 'template_type'
        )

    def validate(self, data):
        """
        Ensure that the necessary fields are filled based on the template type.
        """
        template_type = data.get('template_type')

        if template_type == 'appointment-setter':
            required_fields = ['salesperson_name', 'salesperson_role', 'company_name', 'company_business', 'company_values', 'conversation_purpose']
        elif template_type == 'customer-support':
            required_fields = ['salesperson_name', 'salesperson_role', 'company_name', 'company_business', 'job_role', 'conversation_purpose']
        else:
            required_fields = []

        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: f'{field} is required for {template_type}.'})

        return data

class ListSerializer(serializers.ModelSerializer):
    contact_count = serializers.SerializerMethodField() 

    class Meta:
        model = List
        fields = ['id', 'name', 'contact_count']  

    def get_contact_count(self, obj):
        return Contact.objects.filter(list_id=obj.id).count()


class ContactSerializer(serializers.ModelSerializer):
    list_id = serializers.CharField(source='list_id.name', read_only=True)
    created_at = serializers.DateTimeField(read_only=True) 

    class Meta:
        model = Contact
        fields = ['fullname', 'phone', 'email', 'list_id', 'created_at']

    def validate_phone(self, value):
        if not value:
            raise serializers.ValidationError("Phone number is required.")
        return value
