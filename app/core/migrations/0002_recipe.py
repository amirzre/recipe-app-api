# Generated by Django 3.2.15 on 2022-09-14 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('time_minutes', models.IntegerField(verbose_name='time')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='link')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
