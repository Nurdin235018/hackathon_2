from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .recommendation import *
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register('tickets', TicketsViewSet)
router.register('flights', FlightViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ticket-recommendations/', TicketRecommendationsView.as_view(), name='ticket-recommendations'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls