from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from review.models import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes
from .models import *
from .pagination import *
from .permissions import *
from django.shortcuts import get_object_or_404
from rest_framework import status as http_status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework import generics
import logging
from io import BytesIO
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order
import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings
import os


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.count_views += 1
        instance.save(update_fields=['count_views'])
        return Response(serializer.data)

    @action(['POST'], detail=True)
    def like(self, request, pk=None):
        flight = self.get_object()
        user = request.user
        try:
            like = Like.objects.get(flight=flight, author=user)
            like.delete()
            message = 'disliked'
        except Like.DoesNotExist:
            like = Like.objects.create(flight=flight, author=user)
            like.save()
            message = 'liked'
        return Response(message)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['place']
    ordering_fields = ['id']