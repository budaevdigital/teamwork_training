from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root),
    path('/<int:pk>/highlight', views.ReviewHighlight.as_view()),
    path('comment/<int:pk>/highlight', views.CommentHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
