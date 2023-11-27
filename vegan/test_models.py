from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Recipe, MealPlanItem, Comment

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(admin=self.user, name='Test Category')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            author=self.user,
            description='Test Description',
            ingredients='Test Ingredients',
            method='Test Method',
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, 'Test Recipe')
        self.assertEqual(self.recipe.author, self.user)
        self.assertEqual(self.recipe.description, 'Test Description')
        self.assertEqual(self.recipe.ingredients, 'Test Ingredients')
        self.assertEqual(self.recipe.method, 'Test Method')

class MealPlanItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            author=self.user,
            description='Test Description',
            ingredients='Test Ingredients',
            method='Test Method',
        )
        self.meal_plan_item = MealPlanItem.objects.create(
            user=self.user,
            recipe=self.recipe,
            day=0,
            approved=False,
        )

    def test_meal_plan_item_creation(self):
        self.assertEqual(self.meal_plan_item.user, self.user)
        self.assertEqual(self.meal_plan_item.recipe, self.recipe)
        self.assertEqual(self.meal_plan_item.day, 0)
        self.assertEqual(self.meal_plan_item.approved, False)

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            author=self.user,
            description='Test Description',
            ingredients='Test Ingredients',
            method='Test Method',
        )
        self.comment = Comment.objects.create(
            recipe=self.recipe,
            name='Test Name',
            email='test@example.com',
            body='Test Body',
            approved=False,
        )

    def test_comment_creation(self):
        self.assertEqual(self.comment.recipe, self.recipe)
        self.assertEqual(self.comment.name, 'Test Name')
        self.assertEqual(self.comment.email, 'test@example.com')
        self.assertEqual(self.comment.body, 'Test Body')
        self.assertEqual(self.comment.approved, False)
