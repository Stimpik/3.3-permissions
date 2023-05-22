from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator


class DraftOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user != obj.creator and obj.status == 'DRAFT':
            return False
        else:
            return True
