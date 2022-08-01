from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('reviews/', views.review_list),
    path('reviews/<int:pk>', views.review_detail),
    path('comments/', views.comment_list),
    path('comments/<int:pk>', views.comment_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
