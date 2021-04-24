from django.contrib import admin

from .models import Tweet, Follow


class TweetAdmin(admin.ModelAdmin):
    pass

class FollowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Follow, FollowAdmin)
