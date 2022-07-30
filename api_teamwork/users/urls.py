from django.urls import path
from users.viewsets import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("/api/v1/auth/signup/", UserViewSet, basename="customuser")


urlpatterns = [] 