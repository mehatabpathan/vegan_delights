"""Models"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from .validators import textfield_not_empty


STATUS = ((0, "Draft"), (1, "Publish Now"))


class Category(models.Model):
    """
    Model for Category
    """
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Model for Recipe"""
    title = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    preparation_time = models.CharField(max_length=10, default=0)
    cook_time = models.CharField(max_length=10, default=0)
    description = models.TextField()
    ingredients = models.TextField(validators=[textfield_not_empty])
    method = models.TextField(validators=[textfield_not_empty])
    image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='likes', default=None, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    bookmarks = models.ManyToManyField(
        User, related_name='bookmark', default=None, blank=True)

    class Meta:
        """To display the recipes by created_on in descending order"""
        ordering = ['-created_on']

    def get_absolute_url(self):
        """Get url after user adds/edits recipe"""
        return reverse('recipe_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class MealPlanItem(models.Model):
    """Model for Meal Plan Item"""
    DAY_CHOICES = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="meal_plan")
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="meal_plan_item")
    day = models.IntegerField(choices=DAY_CHOICES, default='0')
    approved = models.BooleanField(default=False)

    class Meta:
        """To display the Meal Plan Items by day in ascending order"""
        ordering = ['day']

    def __str__(self):
        return f"Meal Plan for {self.day} by {self.user}"


class Comment(models.Model):
    """Model for Comment"""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ To display the comments by created_on in ascending order """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
        