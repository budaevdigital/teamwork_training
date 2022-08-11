from rest_framework.routers import SimpleRouter
from django.urls import include, path
from users import viewsets

app_name = "users"

router = SimpleRouter()
router.register("users", viewsets.CustomUserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api/v1/auth/signup/', viewsets.SignUpUser.as_view(), name='signup'),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    ]
