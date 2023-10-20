from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from tickets.models import Tickets
from .models import Order
from .utils import send_confirmation_email
import logging

logger = logging.getLogger(__name__)

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def place_order(request, ticket_id):
        if request.method == 'POST':
            customer_name = request.POST.get('name')
            customer_email = request.POST.get('email')
            ticket = Tickets.objects.get(pk=ticket_id)
            total_price = ticket.price

            order = Order(
                customer_name=customer_name,
                customer_email=customer_email,
                ticket=ticket,
                total_price=total_price,
            )
            order.save()

            send_confirmation_email(order)

            return Response('You got your order')
        return Response('Something is wrong')


