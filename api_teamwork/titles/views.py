from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, renderers

from .models import Title
from .serializers import TitleSerializer
from users.permissions import AdminStaffOnly, AdminOrReadOnly, AuthorModeratorAdminOrSafeMethodOnly


class TitleList(generics.ListCreateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AdminOrReadOnly, )


class TitleUpdate(generics.RetrieveUpdateAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AuthorModeratorAdminOrSafeMethodOnly, AdminStaffOnly)


class TitleDestroy(generics.RetrieveDestroyAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (AdminStaffOnly, AuthorModeratorAdminOrSafeMethodOnly)


class TitleHighlight(generics.GenericAPIView):
    queryset = Title.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        title = self.get_object()
        return Response(title.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'title': reverse('title-list', request=request, format=format),
    })
