# Generated by Django 4.2.7 on 2023-11-15 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegan', '0006_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplanitem',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish Now')], default=0),
        ),
    ]
