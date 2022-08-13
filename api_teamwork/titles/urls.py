from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('title-api-root/', views.api_root),
    path('title/', views.TitleList.as_view()),
    path('title/<int:pk>/', views.TitleUpdate.as_view()),
    path('title-delete/<int:pk>/', views.TitleDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
