from django.contrib import admin
from .models import *
# Register your models here.


class CommentsInline(admin.StackedInline):
    model = Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'views', 'daily_views', 'published_date', 'category')
    inlines = [
        CommentsInline,
    ]


class MessageInline(admin.StackedInline):
    model = Messages


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'started', 'status')
    inlines = [
        MessageInline,
    ]


admin.site.register(Author)
admin.site.register(Posts, PostAdmin)
admin.site.register(Category)

admin.site.register(Threads, ThreadAdmin)
admin.site.register(Comments)
admin.site.register(Messages)
admin.site.register(Portfolio_skills)
admin.site.register(Portfolio_projects)
