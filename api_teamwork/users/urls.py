from rest_framework.routers import SimpleRouter
from django.urls import include, path
from users import viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "users"

router = SimpleRouter()
router.register("users", viewsets.CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api/v1/auth/signup/', viewsets.SignUpUser.as_view(), name='signup'),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    ]
