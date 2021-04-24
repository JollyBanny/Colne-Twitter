from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedDefaultRouter
from twitter.api.router import SwitchDetailRouter
from twitter.api import views

switch_router = SwitchDetailRouter()
router = ExtendedDefaultRouter()

user_route = router.register(r'users', views.UserViewSet)
user_route.register('tweets', views.UserTweetViewSet, 'user-tweets', ['username'])
user_route.register('follows', views.UserFollowsViewSet, 'user-follows', ['username'])
user_route.register('followed', views.UserFollowerViewSet, 'user-follower', ['username'])
router.register(r'tweets', views.TweetViewSet)
router.register(r'feed', views.FeedTweetViewSet)
switch_router.register(r'follow', views.FollowViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(switch_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
