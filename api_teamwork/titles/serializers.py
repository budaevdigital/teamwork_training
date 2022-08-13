from rest_framework import serializers
from .models import Title


class TitleSerializer(serializers.Serializer):
    class Meta:
        model = Title
        fields = ('id', 'category', 'genre', 'name', 'date_release')
