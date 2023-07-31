from rest_framework import serializers
from .models import BlogModel


class ShowBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['title', 'blog_image', 'blog_content', 'author']


class AddBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class ShowBlogDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class PutBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class PatchBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'
