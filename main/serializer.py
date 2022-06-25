from rest_framework import serializers
from .models import *

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'



class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # depth = 1
        model = Product
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Card
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Wishlist
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


seria = serializers.ModelSerializer


class ContactUsSerizlizer(seria):
    class Meta:
        model = ContactUs
        fields = "__all__"


class WishlistSerizlizer(seria):
    class Meta:
        model = Wishlist
        fields = "__all__"


class CardSerizlizer(seria):
    class Meta:
        model = Card
        fields = "__all__"


class ReplySerizlizer(seria):
    class Meta:
        model = Reply
        fields = "__all__"


class CommentSerizlizer(seria):
    # replay_comment = ReplySerizlizer(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"


class BlogtextSerizlizer(seria):
    class Meta:
        model = Blogtext
        fields = "__all__"

class BlogSerializer(seria):
    class Meta:
        model = Blog
        fields = "__all__"


class AboutSerizlizer(seria):
    class Meta:
        model = About
        fields = "__all__"


class AbouttextSerizlizer(seria):
    class Meta:
        model = Abouttext
        fields = "__all__"


class Delivery_OptionsSerizlizer(seria):
    class Meta:
        model = Delivery_Options
        fields = "__all__"


class OrderSerizlizer(seria):
    class Meta:
        model = Order
        fields = "__all__"



















# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['is_active']