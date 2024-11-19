from django.contrib import admin
from .models import *
from .models import (User,UserToken,PromptRecord,TwilioInfo,
                     AgentResponse)

admin.site.register(User) 
admin.site.register(UserToken)
admin.site.register(PromptRecord)
admin.site.register(TwilioInfo)
admin.site.register(List)
admin.site.register(Contact)
admin.site.register(AgentResponse)

