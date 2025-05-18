# auth/utils.py

from itsdangerous import URLSafeTimedSerializer
from flask import current_app, url_for
from flask_mail import Message
from ..extensions import mail


def generate_reset_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt='password-reset-salt')


def verify_reset_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=expiration)
        return email
    except:
        return None


def send_reset_email(user):
    token = generate_reset_token(user.email)
    msg = Message('Password Reset Request',
                  sender='noreply@yourproject.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('auth.reset_password', token=token, _external=True)}
    If you did not make this request, please ignore this email.'''
    mail.send(msg)
