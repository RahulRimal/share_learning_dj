from string import digits
from tkinter import CASCADE
from django.db import models

from django.conf import settings

from django.core.validators import MinValueValidator

# Create your models here.


class Customer(models.Model):
    description = models.TextField(null=True, blank=True)
    # picture = models.FileField
    user_class = models.CharField(max_length=20, blank=True, null=True)
    # followers = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to = 'customer/images', null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def username(self):
        return self.user.username

    def created_at(self):
        return self.user.date_joined

    def __str__(self):
        return f"{self.user.id} => {self.user.first_name} {self.user.last_name}"


# class Follower(models.Model):
#     user = models.OneToOneField(Customer, on_delete=models.CASCADE)
#     following = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Post(models.Model):

    POST_TYPE_BUYING = 'B'
    POST_TYPE_SELLING = 'S'

    POST_TYPE_CHOICES = [
        (POST_TYPE_BUYING, 'Buying'),
        (POST_TYPE_SELLING, 'Selling'),
    ]

    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    bought_date = models.DateField()
    unit_price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(1)])
    book_count = models.PositiveSmallIntegerField(default=1, blank=True)
    # pictures
    wishlisted = models.BooleanField()
    post_type = models.CharField(
        max_length=1, choices=POST_TYPE_CHOICES, default=POST_TYPE_SELLING)
    post_rating = models.FloatField(null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.id} -> {self.book_name}'


class PostImage(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post/images')



class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def post_id(self):
        return self.post.id