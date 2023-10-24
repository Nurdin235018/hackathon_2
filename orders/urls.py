from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('orders', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('confirm/', OrderActivationAPIView.as_view()),
    path('user-order-history/', UserOrderHistoryAPIView.as_view()),
    path('get/<str:name>/', UserActionHistoryAPIView.as_view()),
]
