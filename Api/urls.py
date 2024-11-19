from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *


router= DefaultRouter()
router.register("auth", UserAuthViewset, basename="auth")
router.register("userprofile", UserProfileViewset, basename="userprofile")
router.register("create_agent", CreateAgent, basename="create_agent")
router.register("Logs", Logviewset, basename="Logs")
router.register("list", ListViewSet, basename="list")
router.register("contacts", ContactViewSet, basename="contacts")



urlpatterns = [

]

urlpatterns += router.urls