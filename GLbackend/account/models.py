from typing import Any
import uuid #unique identification for the users

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.timesince import timesince
from django.utils import timezone




class CustomUserManager(UserManager): 
    def _create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("you have not provided a valid email address :<")
        
        email = self.normalize_email(email)
        user =self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin): #user model for creating users from models
    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False) #uses the uuid from the top
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank = True, default='')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    friends = models.ManyToManyField('self')
    friends_count = models.IntegerField(default=0)
    
    
    people_you_may_know = models.ManyToManyField('self')
    
    posts_count = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True) #checking if the user is active, soon set to false for verification
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank = True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_avatar(self):
        if self.avatar:
            return settings.WEBSITE_URL + self.avatar.url
        else:
            return 'https://picsum.photos/200/300'

class FriendshipRequest(models.Model):
    SENT = 'sent'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    STATUS_CHOICES = (
        (SENT, 'sent'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected'),
    )


    id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now_add=True) 
    created_for = models.ForeignKey(User, related_name='received_friendshiprequests', on_delete=models.CASCADE) #friend request sent to
    created_by = models.ForeignKey(User, related_name='created_friendshiprequests', on_delete=models.CASCADE) #who made the friend request
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SENT)