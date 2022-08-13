from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, renderers
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer
from users.permissions import AdminStaffOnly, AdminOrReadOnly, AuthorModeratorAdminOrSafeMethodOnly


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AdminOrReadOnly, )


class ReviewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AuthorModeratorAdminOrSafeMethodOnly, AdminStaffOnly)


class ReviewDestroy(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AdminStaffOnly, AuthorModeratorAdminOrSafeMethodOnly)


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AdminOrReadOnly,)


class CommentUpdate(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorModeratorAdminOrSafeMethodOnly, AdminStaffOnly)


class CommentDestroy(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AdminStaffOnly, AuthorModeratorAdminOrSafeMethodOnly)


class ReviewHighlight(generics.GenericAPIView):
    queryset = Review.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        review = self.get_object()
        return Response(review.highlighted)


class CommentHighlight(generics.GenericAPIView):
    queryset = Comment.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        comment = self.get_object()
        return Response(comment.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'review': reverse('review-list', request=request, format=format),
        'comment': reverse('comment-list', request=request, format=format)
    })
