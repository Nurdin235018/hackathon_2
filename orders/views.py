from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from tickets.serializers import *
from .serializers import *
from review.serializers import *
from tickets.models import *
from review.models import *
from tickets.pagination import *
from tickets.permissions import *
from django.shortcuts import get_object_or_404
from rest_framework import status as http_status
from rest_framework import viewsets, status
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Order
import logging

logger = logging.getLogger(__name__)

# class OrderViewSet(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]
#
#     @action(detail=True, methods=['post'])
#     def place_order(self, request, pk):
#         if request.method == 'POST':
#             email = request.data.get('email')
#             total_price = request.data.get('total_price')
#             try:
#                 ticket = Tickets.objects.get(pk=pk)
#             except Tickets.DoesNotExist:
#                 return Response('Ticket not found', status=status.HTTP_404_NOT_FOUND)
#             order = Order(
#                 email=email,
#                 total_price=total_price,
#                 ticket=ticket
#             )
#             order.save()
#             send_confirmation_email(order)
#
#             return Response('You got your order')
#         return Response('Something is wrong')


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=self.request.user)

        return Response('Заказ успешно создан, но требует подтверждения.', status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderActivationAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        data = request.data
        serializer = OrderConfirmSerializer(data=data)
        if serializer.is_valid():
            serializer.activate()
            return Response('Заказ успешно подтвержден', status=200)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=400)


class UserOrderHistoryAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')


class UserActionHistoryAPIView(APIView):
    def get(self, request, name):
        if name == "like":
            likes = Like.objects.filter(owner=request.user)

            liked_posts = []

            for like in likes:
                post = like.flight

                post_data = {
                    "id": post.id,
                    "title": post.where_to,
                }
                liked_posts.append(post_data)

            return Response({"liked_posts": liked_posts})

        elif name == "favorite":
            favorites = Favourites.objects.filter(author=request.user)

            favorite_posts = []

            for favorite in favorites:
                post = favorite.ticket

                post_data = {
                    "id": post.id,
                    "title": post.where_to,
                }
                favorite_posts.append(post_data)

            return Response({"favorite_posts": favorite_posts})

        elif name == "rating":

            ratings = Rating.objects.filter(author=request.user)

            rated_posts = []

            for rating in ratings:
                post = rating.flight

                post_data = {
                    "id": post.id,
                    "title": post.where_to,
                    "rating": rating.rating,
                }
                rated_posts.append(post_data)

            return Response({"rated_posts": rated_posts})

        elif name == "comment":

            comments = Comment.objects.filter(author=request.user)

            commented_posts = []

            for comment in comments:
                post = comment.flight
                post_data = {
                    "id": post.id,
                    "title": post.where_to,
                    "commented_at": comment.created_at,
                }
                commented_posts.append(post_data)

            return Response({"commented_posts": commented_posts})

        return Response("Invalid action name", status=status.HTTP_400_BAD_REQUEST)

