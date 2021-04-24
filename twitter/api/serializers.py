from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tweet, Follow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'last_name', 'first_name']
        extra_kwargs = {'url': {'lookup_field': 'username'}}

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = []

class UserFollowsSerializer(serializers.ModelSerializer):
    follows = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Follow
        fields = ['follows', 'followed']

class UserFollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Follow
        fields = ['follower', 'followed']


class TweetSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'url', 'text', 'photo', 'created', 'author']