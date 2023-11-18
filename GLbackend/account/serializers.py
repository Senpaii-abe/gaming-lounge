
from rest_framework import serializers

from .models import User, FriendshipRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'friends_count', 'posts_count', 'get_avatar', 'pref_game_category', 'pref_game_titles')

class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'created_by',)
        
