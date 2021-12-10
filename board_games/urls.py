"""Defines URL patterns for board_games."""
from django.urls import path
from . import views

app_name = "board_games"

urlpatterns = [
    # Home page
    path ('', views.index, name='index'),
    # Page that shows all board games
    path('games/', views.games, name='games'),
    # Detail page for a single board game
    path('games/<int:game_id>/', views.game, name='game'),
]