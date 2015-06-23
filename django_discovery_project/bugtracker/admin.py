from django.contrib import admin
from bugtracker.models import Issue, Comment

admin.site.register(Comment)
admin.site.register(Issue)

# Register your models here.
class CommentInline(admin.TabularInline):
	model = Comment

class IssueAdmin(admin.ModelAdmin):
	inlines = [CommentInline,]
