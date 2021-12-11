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

    # Page for adding a new board game
    path('new_game/', views.new_game, name='new_game'),

    # Page for adding a description
    path('new_description/<int:game_id>/', views.new_description, name='new_description'),

    # Page for editing a description
    path('edit_description/<int:description_id>/', views.edit_description, name='edit_description'),

    # Page for adding a new loaner for a specific game
    path('new_loaner/<int:game_id>/', views.new_loaner, name='new_loaner'),
]