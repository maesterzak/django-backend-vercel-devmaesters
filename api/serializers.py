from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    posts_comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Posts
        fields = ['title','id','author', 'body', 'published_date', 'posts_comments', 'views', 'category', 'image', 'tags', 'video', 'daily_views', 'updated_date']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'



class ThreadsSerializer(serializers.ModelSerializer):
    thread_messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Threads
        fields = ['title', 'id', 'description', 'thread_messages', 'status', 'started']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['username, first_name' ]


class PortfolioSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio_skills
        fields = '__all__'


class PortfolioProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio_projects
        fields = '__all__'

