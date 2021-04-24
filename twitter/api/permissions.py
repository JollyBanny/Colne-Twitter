from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTweetAuthReadOnly(BasePermission):
    def has_object_permission(self, request, view, tweet):
        if request.method in SAFE_METHODS:
            return True
        if request.user and \
            request.user.is_authenticated and \
            tweet.author == request.user:
            return True
        return False