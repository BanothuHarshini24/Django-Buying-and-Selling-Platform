# Generated by Django 4.1.7 on 2023-04-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olx', '0003_week_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bid_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
