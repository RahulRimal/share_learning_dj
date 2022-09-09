from rest_framework import serializers


from .models import Customer, Post


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id')
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'description', 'user_class']

class SimpleCustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id')
    class Meta:
        model = Customer
        # model = User
        fields = ['id', 'first_name', 'last_name', 'email']



class PostSerializer(serializers.ModelSerializer):
    user = SimpleCustomerSerializer(read_only=True)
    # user = SimpleCustomerSerializer()
    # id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'book_name', 'author', 'description', 'bought_date', 'unit_price', 'book_count', 'wishlisted', 'post_type', 'post_rating', 'posted_on']