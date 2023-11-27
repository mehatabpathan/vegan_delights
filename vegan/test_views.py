from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from .models import Recipe, Comment, MealPlanItem


class ViewsTest(TestCase):
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
            approved=True,
        )
        self.meal_plan_item = MealPlanItem.objects.create(
            user=self.user,
            recipe=self.recipe,
            day=0,
            approved=False,
        )
        # self.login_url = reverse('login')
        self.recipe_list_url = reverse('recipe_list')
        self.recipe_detail_url = reverse('recipe_detail', kwargs={'slug': self.recipe.slug})
        self.add_recipe_url = reverse('add_recipe')
        
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_recipe_list_view(self):
        response = self.client.get(self.recipe_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'browse_recipes.html')

    def test_recipe_detail_view(self):
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

    def test_add_recipe_view_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.add_recipe_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    