from django.db import models

# Create your models here.
from account.models import User

class Situation(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return f'{self.name}'

class Place(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return f'{self.name}'

class GameType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return f'{self.name}'


class Game(models.Model):
    title = models.CharField(max_length=30, null=False)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='game')
    created_at = models.DateField(auto_now_add=True)
    #modified_at = models.DateTimeField(auto_now=True)

    min_num_ppl = models.IntegerField( null=True)
    max_num_ppl = models.IntegerField(null=True)
    min_time = models.CharField(max_length=30, null=True)
    max_time = models.CharField(max_length=30, null=True)
    situation = models.ForeignKey(Situation, null=False, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, null=False, on_delete=models.CASCADE)
    game_type = models.ManyToManyField(GameType)

    preparation = models.TextField(null=False)
    explanation = models.TextField(null=False)
    tip = models.TextField()

    image = models.ImageField(upload_to="images/games/", null=True, blank=True)
    likes = models.ManyToManyField('Like', related_name='game', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def likes_count(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='like')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'