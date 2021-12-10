from django.shortcuts import render

from .models import Game

# Create your views here.

def index (request):
    """The home page for Board Games"""
    return render(request, 'board_games/index.html')


def games(request):
    """Show all games"""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_games/games.html', context)

def game(request, game_id):
    """Show a single board game and its description."""
    game = Game.objects.get(id=game_id)
    descriptions = Game.description_set.order_by('-date_added')
    context = {'game': game, 'descriptions': descriptions}
    return render(request, 'board_games/game.html', context)
