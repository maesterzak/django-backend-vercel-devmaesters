from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', all_posts, name='task-list'),
    path('post-detail/<str:pk>/', post_detail, name='post_detail'),
    path('post-create/', post_create, name='post_create'),
    path('post-update/<str:pk>/', post_update, name='post_update'),
    path('post-delete/<str:pk>/', post_delete, name='post_delete'),
    path('categories/', all_categories, name='categories-list'),
    path('categories-posts/<str:str>/', all_category_post, name='category_post'),
    path('threads/', all_threads, name='all_threads'),
    path('thread-detail/<str:pk>/', thread_detail, name='thread_detail'),
    path('thread-create/', thread_create, name='thread_create'),
    path('message-create/', message_create, name='message_create'),
    path('comment-create/', comment_create, name='comment_create'),
    path('register/', register.as_view(), name='register'),
    path('user/', loaduserview.as_view(), name='user'),

]