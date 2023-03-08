from django.core.exceptions import ValidationError
import re

def password_validation(password):
    min_len = 9
    flag = 0
    while True:
        if len(password) <= 8:
            flag = -1
            raise ValidationError(f'password must be {min_len} characters long')

        elif not re.search('[a-z]',password):
            flag = -1
            raise ValidationError(f'password must contain a-z')

        elif not re.search('[A-Z]',password):
            flag = -1
            raise ValidationError(f'password must be at least one caps')

        elif not re.search('\d',password):
            flag = -1
            raise ValidationError(f'password must contain numbers 0-9')

        elif not re.search('[_@$]',password):  
            flag = -1
            raise ValidationError(f'password must have special characters')

        elif re.search('\s',password):
            flag = -1
            raise ValidationError(f'password must not contain spaces')

        else:
            flag = 0
            break
