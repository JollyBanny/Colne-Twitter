from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Tweet, Follow
from .serializers import UserSerializer, TweetSerializer, FollowSerializer, UserFollowsSerializer, UserFollowerSerializer
from .permissions import IsTweetAuthReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all().order_by('-created')
    serializer_class = TweetSerializer
    permission_classes = [
        IsTweetAuthReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserTweetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get_queryset(self):
        return self.queryset.filter(author__username = self.kwargs['parent_lookup_username'])

class UserFollowsViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Follow.objects
    serializer_class = UserFollowsSerializer

    def get_queryset(self):
        username = self.kwargs['parent_lookup_username']
        return self.queryset.filter(
            follower__username=username
        )

class UserFollowerViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Follow.objects
    serializer_class = UserFollowerSerializer

    def get_queryset(self):
        username = self.kwargs['parent_lookup_username']
        return self.queryset.filter(
            follows__username=username
        )

class FeedTweetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        queryset = queryset.filter(Q(author__follower__follower = self.request.user) | Q(author__username = self.request.user.username))
        return queryset

class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    queryset = Follow.objects
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        follows = User.objects.get(username=self.kwargs[self.lookup_field])
        serializer.save(follower=self.request.user, follows=follows)

    def get_object(self):
        return self.queryset.filter(
            follower=self.request.user,
            follows__username=self.kwargs[self.lookup_field],
        )