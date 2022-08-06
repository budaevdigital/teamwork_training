from rest_framework.routers import DefaultRouter
from django.urls import include, path
from users.viewsets import UserViewSet

app_name = "users"

router = DefaultRouter()
router.register("auth/signup/", UserViewSet, basename="customuser")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    ]
