# Generated by Django 4.2.6 on 2023-11-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_game_image_alter_game_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='game', to='game.like'),
        ),
    ]
