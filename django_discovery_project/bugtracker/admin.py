from django.contrib import admin
from bugtracker.models import Issue, Comment



# Register your models here.
class CommentInline(admin.TabularInline):
     model = Comment


class IssueAdmin(admin.ModelAdmin):
     inlines = [CommentInline,]


admin.site.register(Issue, IssueAdmin)
