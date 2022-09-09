from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Customer, Post


from .serializers import CustomerSerializer, PostSerializer


# Create your views here.


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.select_related('user').all()
    serializer_class = CustomerSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.select_related('user').all()
    # queryset = Post.objects.prefetch_related('user').all()

    serializer_class = PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_context(self):
        return {'request': self.request}


    def update(self, request, *args, **kwargs):
        logged_in_user  = request.user
        post_user_id = request.data['user_id']

        if(int(post_user_id) != logged_in_user.id):
            return Response({'error': 'You can edit only your posts!!'})
        
        # return super().update(self, request, *args, **kwargs)
        return super().update(request)

