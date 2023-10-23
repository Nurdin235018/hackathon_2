from rest_framework import generics
from .models import Tickets
from .serializers import TicketsSerializer


class TicketRecommendationsView(generics.ListAPIView):
    serializer_class = TicketsSerializer

    def get_queryset(self):
        return Tickets.objects.all()