from django.contrib.auth import get_user_model

User = get_user_model()

def delete_patient_data(patient_email):
    if User.objects.filter(email=patient_email).exists():
        User.objects.filter(email=patient_email).delete()