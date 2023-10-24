from django.core.mail import send_mail


# def send_confirmation_email(order):
#     email=order.email
#     subject = 'Flight Order Confirmation'
#     message = 'Dear client,\n\n' \
#               f'Thank you for placing an order for a flight with us. Your order details are as follows:\n' \
#               f'Flight: {order.tickets.flight}\n' \
#               f'Total Price: {order.total_price}\n\n' \
#               f'Place: {order.ticket.place}\n\n' \
#               f'We appreciate your business. Safe travels!'
#     from_email = 'test@gmail.com'
#     to_email = [email]
#
#     send_mail(subject, message, from_email, to_email, fail_silently=False)


def send_order_email(email, code, name):
    send_mail(
        'aviasales',
        f'Hello {name}, this is your code: {code}',
        'taabaldyev.nurdin27@mail.ru',
        [email]
    )