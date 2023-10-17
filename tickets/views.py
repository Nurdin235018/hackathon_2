from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


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
    lookup_field = 'pk'
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['title']
    search_fields = ['title']
    pagination_class = PostSetPagination