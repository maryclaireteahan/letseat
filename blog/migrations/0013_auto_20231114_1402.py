# Generated by Django 3.2.23 on 2023-11-14 14:02

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=djrichtextfield.models.RichTextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=djrichtextfield.models.RichTextField(blank=True, max_length=10000, null=True),
        ),
    ]
