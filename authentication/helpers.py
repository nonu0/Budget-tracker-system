from django.utils.crypto import get_random_string
import hashlib


def generate_activation_key(username):
    values = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20,values)
    print('secret',secret_key)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()