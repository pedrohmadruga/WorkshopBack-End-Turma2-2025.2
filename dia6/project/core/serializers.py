from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source='user_id')

    class Meta:
        model = Post
        fields = ['userId', 'title', 'body']