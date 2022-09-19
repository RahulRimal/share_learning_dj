from urllib import request
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.decorators import action

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .permissions import IsPostOwner, IsSuperOrHasCustomerPermissions, IsSuperOrHasPostPermissionsOrReadOnly, IsSuperUser

from .models import Customer, Post, PostImage


from .serializers import CustomerSerializer, PostImageSerializer, PostSerializer
from store import serializers


# Create your views here.


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.select_related('user').all()
    serializer_class = CustomerSerializer
    permission_classes = [IsSuperOrHasCustomerPermissions]

    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [IsSuperUser()]
    #     return [IsAuthenticated()]

    @action(detail=False, methods=['GET', 'PATCH'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('user').all()
    # queryset = Post.objects.prefetch_related('user').all()

    serializer_class = PostSerializer

    permission_classes = [IsPostOwner]
    # permission_classes = [IsSuperOrHasPostPermissionsOrReadOnly]

    def get_serializer_context(self):
        return {'request': self.request}

    def update(self, request, *args, **kwargs):
        logged_in_user = request.user
        post_user_id = request.data['user_id']

        if (int(post_user_id) != logged_in_user.id):
            return Response({'error': 'You can edit only your posts!!'})

        # return super().update(self, request, *args, **kwargs)
        return super().update(request)


class PostImageViewSet(ModelViewSet):
    # queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_queryset(self):
        return PostImage.objects.filter(post_id=self.kwargs['post_pk'])

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}
