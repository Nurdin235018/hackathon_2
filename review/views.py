import logging

from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from review.models import Comment, Rating
from review.serializers import CommentSerializer, RatingSerializer

logger = logging.getLogger(__name__)

import logging

logger = logging.getLogger(__name__)


def my_view(request):
    # Ваш код
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer