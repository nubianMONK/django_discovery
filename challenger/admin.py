from django.contrib import admin
from challenger.models import MainCategory, Challenge, Issue, Solution

# Register your models here.

class ChallengeInline(admin.TabularInline):
	model = Challenge

class IssueInline(admin.TabularInline):
	model = Issue


class SolutionInline(admin.TabularInline):
	model = Solution


class MainCategoryAdmin(admin.ModelAdmin):
	Inlines = [ChallengeInline,IssueInline,SolutionInline,]

admin.site.register(MainCategory,MainCategoryAdmin)
