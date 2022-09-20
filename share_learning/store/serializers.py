from rest_framework import serializers


from .models import Customer, Post, PostComment, PostImage


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id', read_only=True)
    # class' = serializers.CharField(source='user_class')

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name',
                  'username', 'email', 'description', 'image', 'user_class', 'created_at']


class SimpleCustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user_id', read_only=True)

    class Meta:
        model = Customer
        # model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class PostImageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        post_id = self.context['post_id']
        return PostImage.objects.create(post_id=post_id, **validated_data)

    class Meta:
        model = PostImage
        fields = ['id', 'image']


class PostSerializer(serializers.ModelSerializer):
    user = SimpleCustomerSerializer(read_only=True)
    # user = SimpleCustomerSerializer()
    # id = serializers.IntegerField(read_only=True)
    images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'book_name', 'author', 'description', 'bought_date',
                  'unit_price', 'book_count', 'images', 'wishlisted', 'post_type', 'post_rating', 'posted_on']


class PostCommentSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(source='user_id', read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = PostComment
        fields = ['id', 'user_id', 'post_id', 'comment_body', 'created_date']