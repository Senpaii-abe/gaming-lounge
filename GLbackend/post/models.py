import uuid

from django.conf import settings
from django.db import models
from django.utils.timesince import timesince
from django.utils import timezone
from django.apps import apps
from account.models import User
from django.contrib.auth import get_user_model
from django.db import models

class Like(models.Model): #can reuse for liking pages or what (universal)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)
    
    def created_at_formatted(self):
        return timesince(self.created_at)
    

# category can't be deleted if there is an existing post about it
# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    

class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)
    
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return ''
    

class Category(models.Model):
    game_category = models.CharField(max_length=255)

class GameTitle(models.Model):
    title = models.CharField(max_length=255, unique=True)
    categories = models.ManyToManyField(Category)
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    
    game_title = models.ForeignKey(GameTitle, on_delete=models.PROTECT, blank=True, null=True)
    
    attachments = models.ManyToManyField(PostAttachment, blank=True)
    
    is_private = models.BooleanField(default=False)
    
    likes = models.ManyToManyField(Like, blank=True)
    likes_count = models.IntegerField(default=0)
    
    comments = models.ManyToManyField(Comment, blank=True)
    comments_count = models.IntegerField(default=0)
    
    reported_by_users = models.ManyToManyField(User, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE) #all post will be deleted when this user is deleted
    
    class Meta: 
        ordering = ('-created_at',) #order ng post sa feed
        
    def created_at_formatted(self):
        return timesince(self.created_at)
    
class Trend(models.Model):
    hashtag = models.CharField(max_length=255)
    occurences = models.IntegerField()

