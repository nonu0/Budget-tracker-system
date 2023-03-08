from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        """creates and saves a user 
           based on email and password provided"""
        if not email:
            raise ValueError('Email must be provided')
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            username = username,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self,email,username,password=None):
        """creates and saves super users"""
        user = self.create_user(email,username,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=50,unique=True)
    username = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    


    def __str__(self):
        return self.email

