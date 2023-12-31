# Generated by Django 4.2.5 on 2023-11-13 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/gamelist/')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posted_gamelist', to=settings.AUTH_USER_MODEL)),
                ('collectors', models.ManyToManyField(blank=True, null=True, related_name='collected_gamelist', to=settings.AUTH_USER_MODEL)),
                ('games', models.ManyToManyField(null=True, to='game.game')),
            ],
        ),
    ]
