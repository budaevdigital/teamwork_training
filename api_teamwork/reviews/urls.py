from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('review-api-root/', views.api_root),
    path('review/', views.ReviewList.as_view()),
    path('review/<int:pk>/', views.ReviewUpdate.as_view()),
    path('review-delete/<int:pk>/', views.ReviewDestroy.as_view()),
    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('comment-delete/<int:pk>/', views.CommentDestroy.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
