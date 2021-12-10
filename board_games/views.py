from django.shortcuts import render, redirect

from .models import Game
from .forms import GameForm, DescriptionForm

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
    descriptions = game.description_set.order_by('-date_added')
    context = {'game': game, 'descriptions': descriptions}
    return render(request, 'board_games/game.html', context)

def new_game(request):
    """Add a new game."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GameForm()
    else:
        # POST data submitted; process data.
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:games')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'board_games/new_game.html', context)

def new_description(request, game_id):
    """Add a new description for a partular board game."""
    game = Game.objects.get(id=game_id)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = DescriptionForm()
    else:
        # POST data submitted, process data.
        form = DescriptionForm(data=request.POST)
        if form.is_valid():
            new_description = form.save(commit=False)
            new_description.game = game
            new_description.save()
            return redirect('board_games:game', game_id=game_id)
    
    # Display a blank or invalid form.
    context = {'game': game, 'form': form}
    return render(request, 'board_games/new_description.html', context)