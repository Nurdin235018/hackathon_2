from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from review.models import Comment, Like
from review.serializers import CommentSerializer, LikeSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    class LikeView(generics.CreateAPIView):
        queryset = Like.objects.all()
        serializer_class = LikeSerializer

        @action(methods=['POST'], detail=True)
        def like(self, request, pk=None):
            post = self.get_object()
            user = request.user
            try:
                like = Like.objects.get(post=post, author=user)
                like.delete()
                message = 'disliked'
            except Like.DoesNotExist:
                like = Like.objects.create(post=post, author=user)
                like.save()
                message = 'liked'
            return Response(message)

    @action(methods=['GET'], detail=True)
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(comments, Many=True)
        return Response(serializer.data)
