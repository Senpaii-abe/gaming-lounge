import uuid

from django.db import models
from django.utils.timesince import timesince

from account.models import User

class PostAttachments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    
    attachments = models.ManyToManyField(PostAttachments, blank=True)
    
    #likes
    #likes_count
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE) #all post will be deleted when this user is deleted
    
    class Meta: 
        ordering = ('-created_at',) #order ng post sa feed
        
    def created_at_formatted(self):
        return timesince(self.created_at)
