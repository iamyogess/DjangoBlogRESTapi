from rest_framework import serializers
from .models import BlogModel


class ShowBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['title', 'blog_content']


class AddBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['title', 'blog_content']


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
