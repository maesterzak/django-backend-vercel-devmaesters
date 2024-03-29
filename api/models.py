import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    about_me = RichTextField()
    profile_image = models.ImageField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkdn = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    whatsapp = models.CharField(blank=True, null=True, max_length=15)



    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Posts(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey(Author, related_name='author',blank=False, null=True, on_delete=models.SET_NULL)
    published_date = models.DateField()
    updated_date = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)
    body = RichTextUploadingField(default='Empty Content')
    handshakes = models.IntegerField(default=0)
    category = models.ForeignKey(Category,related_name='category', blank=False, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(blank=True, null=True)
    daily_views = models.IntegerField(default=0, blank=False)
    tags = ArrayField(models.CharField(null=False, blank=True,max_length=20, default='cat'), default=list)
    publish = models.BooleanField(default=False)
    video = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Threads(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    status = models.BooleanField(default=True)
    started = models.DateField()

    def __str__(self):
        return str(self.title)


class Messages(models.Model):

    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    body = RichTextField()
    thread = models.ForeignKey(Threads,related_name='thread_messages', on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True, null=True)
    profile_image_value = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Comments(models.Model):

    name = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    body = RichTextField()
    post = models.ForeignKey(Posts,related_name='posts_comments', on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True, null=True)
    profile_image_value = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Portfolio_skills(models.Model):
    name = models.CharField(max_length=100)
    svg_image = models.FileField()

    def __str__(self):
        return str(self.name)


class Portfolio_projects(models.Model):
    name = models.CharField(max_length=100)
    stack = models.TextField()
    description = RichTextField()
    video = models.CharField(blank=True, null=True, max_length=300)
    github = models.CharField(blank=True, null=True, max_length=300)
    demo = models.URLField(blank=True, null=True)
    videoSize = models.CharField(blank=True, null=True, max_length=5)


    def __str__(self):
        return str(self.name)