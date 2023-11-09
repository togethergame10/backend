from django.contrib import admin

# Register your models here.
from game.models import Game, Situation, Place, GameType, Like

admin.site.register(Game)

admin.site.register(Place)
admin.site.register(Situation)
admin.site.register(GameType)

admin.site.register(Like)