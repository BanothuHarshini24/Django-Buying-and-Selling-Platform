# Generated by Django 4.1.7 on 2023-04-16 18:25

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='myorders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('post_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='verify_post',
            fields=[
                ('id_post', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='post_images')),
                ('image2', models.ImageField(upload_to='post_images')),
                ('image3', models.ImageField(upload_to='post_images')),
                ('image4', models.ImageField(upload_to='post_images')),
                ('image5', models.ImageField(upload_to='post_images')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('cart', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('verification', models.BooleanField(default=True)),
            ],
        ),
    ]