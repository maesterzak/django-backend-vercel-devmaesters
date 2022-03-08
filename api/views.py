from django.shortcuts import render
from rest_framework import permissions
from .models import *
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status
from django.contrib.auth.models import User
# Create your views here.


@api_view(['GET'])
def all_posts(request):
    posts = Posts.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def post_detail(request, pk):
    post = Posts.objects.get(id=pk)
    post.daily_views=(post.daily_views + 1)
    post.save()

    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def post_create(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
        print('request not valid')
    return Response(serializer.data)


@api_view(['POST'])
def post_update(request, pk):
    post = Posts.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:

        print('request update not valid')
    return Response(serializer.errors)


@api_view(['DELETE'])
def post_delete(request, pk):
    post = Posts.objects.get(id=pk)
    post.delete()
    print('it has been deleted')
    return HttpResponse('Task deleted')


@api_view(['GET'])
def all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def all_threads(request):
    threads = Threads.objects.all()
    serializer = ThreadsSerializer(threads, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def thread_detail(request, pk):
    post = Threads.objects.get(id=pk)
    serializer = ThreadsSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def thread_create(request):
    serializer = ThreadsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
        print('request not valid')
    return Response(serializer.data)


@api_view(['POST'])
def message_create(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
        print('request not valid')
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request):
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        print('message saved')
    else:
        print(serializer.errors)
        print('request not valid')
    return Response(serializer.data)



@api_view(['GET'])
def all_category_post(request, str):

    posts = Posts.objects.filter(category__name=str)

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_portfolio_skills(request):

    skill = Portfolio_skills.objects.all()

    serializer = PortfolioSkillsSerializer(skill, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def all_portfolio_projects(request):
    project = Portfolio_projects.objects.all()
    serializer = PortfolioProjectSerializer(project, many=True)
    return Response(serializer.data)



class register(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):

        data=request.data

        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        password = data['password']
        re_password = data['re_password']
        if password == re_password:
            if len(password) >=8:
                if not User.objects.filter(username=username).exists():
                    user =User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        password = password
                    )
                    author = Author.objects.create(
                        name = first_name
                    )
                    #user.save()
                    if User.objects.filter(username=username).exists():
                        return Response(
                            {'success':'Account created successfully'},
                            status = status.HTTP_201_CREATED
                        )
                    else:
                        return Response(
                            {'error': 'Something went wrong when trying to create'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response (
                        {'error': 'username already exist'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

            else:
                return Response(
                    {'error': 'passwords must be at least 8 char'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        else:
            return Response(
                {'error': 'passwords do not match'},
                status=status.HTTP_400_BAD_REQUEST
            )



class loaduserview(APIView):
    def get(self, request, format=None):
        try:
            user=request.user
            user = UserSerializer(user)
            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'something went wrong when trying to load user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )