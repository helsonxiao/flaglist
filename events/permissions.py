from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only owner can make changes to event belongs to him/her.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user