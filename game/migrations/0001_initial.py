# Generated by Django 4.2.5 on 2023-11-13 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('min_num_ppl', models.IntegerField(null=True)),
                ('max_num_ppl', models.IntegerField(null=True)),
                ('min_time', models.CharField(max_length=30, null=True)),
                ('max_time', models.CharField(max_length=30, null=True)),
                ('preparation', models.TextField()),
                ('explanation', models.TextField()),
                ('tip', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/games/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='game', to=settings.AUTH_USER_MODEL)),
                ('game_type', models.ManyToManyField(to='game.gametype')),
                ('likes', models.ManyToManyField(blank=True, null=True, related_name='game', to='game.like')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.place')),
                ('situation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.situation')),
            ],
        ),
    ]
