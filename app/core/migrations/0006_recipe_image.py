# Generated by Django 3.2.15 on 2022-09-18 06:11

from django.db import migrations, models
import extensions.path


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220917_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=extensions.path.recipe_image_file_path, verbose_name='image'),
        ),
    ]
