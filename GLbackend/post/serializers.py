
from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True) #read only because when we create post we dont want to mess with the created_by field
    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at_formatted',)