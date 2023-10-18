from django.core.mail import send_mail


def send_order_confirm(email, code):
    send_mail('Confirm your order', from_email='test@gmail.com', recipient_list=[email])
    # message = 'This is a test email sent from Django with attachments.'

    # email = EmailMessage(subject, message, from_email, recipient_list)
    # email.attach_file('path/to/attachment.pdf')  # Attach a file
    # email.send()