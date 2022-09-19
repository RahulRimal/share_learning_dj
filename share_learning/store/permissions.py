from urllib import request
from rest_framework import permissions

from .models import Post


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsAuthenticatedAndHasPermitted(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='modirator'):
            return True
        return False


class IsSuperOrHasPostPermissionsOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool((request.user and request.user.groups.filter(name='post_modirator')) or request.user.is_superuser)


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)


class IsSuperOrHasCustomerPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user.is_superuser or request.user.groups.filter(name='customer_modirator'))


class IsPostOwner(permissions.BasePermission):
    def has_permission(self, request, view):

        # user_id = request.user.id
        post_id = view.kwargs.get('pk')

        # if post_id is None and request.method in permissions.SAFE_METHODS:
        # if post_id is None and IsSuperUser():
        if post_id is None:
            if request.method in permissions.SAFE_METHODS:
                return True
            return False

        # post = Post.objects.filter(id=post_id)
        # print(post.values()[0]['user_id'])

        post_user_id = (Post.objects.filter(
            id=post_id)).values()[0]['user_id']

        user_id = request.user.id

        if user_id == post_user_id:
            if request.method in permissions.SAFE_METHODS or request.method == 'PATCH':
                return True
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return False

        
