from django.core.mail import send_mail


def send_conformation_email(user):
    code = user.activation_code
    to_email = user.email
    link = f'http://localhost:8000/api/v1/accounts/activate/{code}'
    send_mail('Hello, wellcome to our shop.', f'To activate your account please follow this link: {link}', 'example@gmail.com', [to_email, ], fail_silently=False)

