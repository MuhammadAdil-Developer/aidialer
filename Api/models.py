from django.db import models

"""
models.py - Defines Django models for the application.

This module contains the definition of Django models representing different entities
in the application, including users, tokens, products, reviews, orders, etc.
"""
import uuid
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """
    An abstract base model with common fields for other models.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, max_length=255
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class User(BaseModel):
    
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="", unique=True)
    profile = models.ImageField(upload_to="User/", default="User/dummy.png")
    password = models.TextField(default="", null=False, blank=False)
    otp = models.IntegerField(default=0)
    otp_count = models.IntegerField(default=0)
    otp_status = models.BooleanField(default=False)
    no_of_attempts_allowed = models.IntegerField(default=3)
    no_of_wrong_attempts = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.email}"
    

class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='', blank=False, null=False)
    token = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f"UserToken(user={self.user}, created_at={self.created_at})"


class PromptRecord(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='', blank=False, null=False)
    assistance_name = models.CharField(max_length=100, default='')
    welcome_message = models.CharField(max_length=555, default='')
    salesperson_name = models.CharField(max_length=100)
    salesperson_role = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_business = models.CharField(max_length=1000)
    company_values = models.CharField(max_length=1000)
    conversation_purpose = models.CharField(max_length=1000)
    conversation_further_information = models.CharField(max_length=2000)
    QNA = models.CharField(max_length=2000)
    conversation_type = models.CharField(max_length=100)
    template_type = models.CharField(max_length=255, choices=[('appointment-setter', 'Appointment Setter'), ('customer-support', 'Customer Support'), ('inbound', 'Inbound'), ('Game NPC', 'Game NPC')])
    generated_prompt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return f"{self.assistance_name}"
 

class TwilioInfo(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='', blank=True, null=True)
    twilio_sid = models.CharField(max_length=50)
    twilio_token = models.CharField(max_length=50)
    twilio_number = models.CharField(max_length=20)
    label_name = models.CharField(max_length=100)

    def __str__(self):
        return self.twilio_sid

class List(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='', blank=True, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contact(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='', blank=True, null=True)
    list_id = models.ForeignKey(List, related_name='contacts', on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=True, null=True)  # Optional
    phone = models.CharField(max_length=20)  # Required
    email = models.EmailField(blank=True, null=True)  # Optional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname if self.fullname else "Unnamed Contact"


# class CallLog(BaseModel):
#     call_sid = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     log_type = models.CharField(max_length=50)
#     message = models.TextField()

# class Transcription(BaseModel):
#     call_sid = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     transcription = models.TextField()

class AgentResponse(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='', blank=True, null=True)
    call_sid = models.CharField(max_length=255)
    call_type = models.CharField(max_length=20, default='')  
    cost = models.FloatField(default='0.0')  
    EndedReason = models.CharField(max_length=20, blank=True, null=True)  
    assistant = models.CharField(max_length=20, blank=True, null=True)  
    from_number = models.CharField(max_length=20, blank=True, null=True)  
    from_number = models.CharField(max_length=20, blank=True, null=True)  
    to_number = models.CharField(max_length=20, blank=True, null=True)    
    log_type = models.CharField(max_length=50,default='')
    messages = models.TextField(default="")  # Store concatenated messages
    start_time = models.DateTimeField(null=True, blank=True)  # Start time of the call
    end_time = models.DateTimeField(null=True, blank=True)  # End time of the call
    response = models.TextField()
    analysis = models.TextField(null=True, blank=True,default='')
    converstional_status = models.CharField(null=True, blank=True, max_length=50,default='')
    


    def __str__(self):
        return f"AgentResponse for Call SID {self.call_sid}"
 