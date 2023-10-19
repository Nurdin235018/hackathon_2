from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import *
from .models import Flight, Category, Tickets
from .serializers import *
from django.utils.decorators import method_decorator
from .permissions import IsAdminPermission


class FlightViewSet(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    # permission_classes = [IsAdminPermission]

    # def create(self, request, *args, **kwargs):
    #     if not request.user.is_superuser:
    #         return Response({'detail': 'Permission Denied'})
    #     return super(FlightViewSet, self).create(request, *args, **kwargs)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class TicketsViewSet(ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title']
    pagination_class = PostSetPagination