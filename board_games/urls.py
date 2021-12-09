"""Defines URL patterns for board_games."""
from django.urls import path
from . import views

app_name = "board_games"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all games
    path('games/', views.games, name= 'games'),

    # Detail page for a single book.
    path('games/<int:game_id>', views.game, name='game'),
]