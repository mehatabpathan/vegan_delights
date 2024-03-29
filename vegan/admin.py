"""imports for admin page"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Recipe, Comment, MealPlanItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Allows admin to manage categories via the admin panel
    """
    list_display = ('admin', 'name')


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Allows admin to manage recipes via the admin panel"""
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'description')
    summernote_fields = ('description', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Allows admin to manage comments on recipes via the admin panel"""
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(MealPlanItem)
class MealplanAdmin(admin.ModelAdmin):
    """Allows admin to manage user meal plans via the admin panel"""
    list_display = ('user', 'recipe', 'day')
    actions = ['approve_mealplan']

    def approve_mealplan(self, request, queryset):
        queryset.update(approved=True)
