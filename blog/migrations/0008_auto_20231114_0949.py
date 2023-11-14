# Generated by Django 3.2.23 on 2023-11-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('dessert', 'Dessert'), ('snack', 'Snack')], max_length=80),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(related_name='recipes', to='blog.Category'),
        ),
    ]
