# Generated by Django 4.1.7 on 2023-04-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0002_myorders_verify_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='week_bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('post_id', models.CharField(max_length=100)),
            ],
        ),
    ]
