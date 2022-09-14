from urllib import request
from rest_framework import permissions


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
        return bool(request.user.is_superuser or request.user.groups.filter(name='customer_modirator'))
