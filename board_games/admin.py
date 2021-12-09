from django.contrib import admin
from board_games.models import Game, Description

# Register your models here.


admin.site.register(Game)
admin.site.register(Description)