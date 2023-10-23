from django.core.mail import send_mail


def send_code(email, code):
    send_mail('Activation of account', f'You successfully login in our site. Activate code: {code}', 'test@gmail.com', [email])


def send_activation_code(email, code):
    send_mail(
        'AviaSales',
        f'Привет перейди по этой ссылке чтобы активировать аккаунт: '
        f'\n\n http://localhost:8000/api/account/activate/{code}',
        'taabaldyev.nurdin27@mail.ru',
        [email]
    )


def send_new_password(user, new_password):
    send_mail(
        'Ваш пароль успешно сброшен',
        f'Это ваш код подверждение: {new_password}'
        f'Перейдите по этой сслыке что-бы создать новый пароль код поставьте вместо current_password '
        f'\n\n localhost:8000/api/account/change_password/',
        'taabaldyev.nurdin27@mail.ru',
        [user.email],
        fail_silently=False,
    )
