from django.shortcuts import render

from .models import Game

# Create your views here.

def index(request):
    """The home page for Board Games."""
    return render(request, 'board_games/index.html')

def games(request):
    """Show all board games."""
    games = Game.objects.order_by('text')
    context = {'games': games}
    return render(request, 'board_games/games.html', context)
