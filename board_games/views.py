from django.shortcuts import render, redirect


from .models import Game, Description, Loaner
from .forms import GameForm, DescriptionForm, LoanerForm
from django.contrib.auth.decorators import login_required  # -emilia


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
    loaners = game.loaner_set.order_by('-date_added')
    context = {'game': game, 'descriptions': descriptions, 'loaners': loaners}
    return render(request, 'board_games/game.html', context)

@login_required
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

@login_required
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

@login_required
def edit_description(request, description_id):
    """Edit an existing description."""
    description = Description.objects.get(id=description_id)
    game = description.game

    if request.method != 'POST':
        # Initial request; pre-fill form with the current description.
        form = DescriptionForm(instance=description)
    else:
        # POST data submitted; process data.
        form = DescriptionForm(instance=description, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:game', game_id=game.id)
    
    context = {'description': description, 'game': game, 'form': form}
    return render(request, 'board_games/edit_description.html', context)


@login_required
def new_loaner(request, game_id):
    """Add a new description for a partular board game."""
    game = Game.objects.get(id=game_id)

    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = LoanerForm()
    else:
        # POST data submitted, process data.
        form = LoanerForm(data=request.POST)

        if form.is_valid():
            game.loan_status = 'U'
            new_loaner = game.loaner
            new_loaner = form.save(commit=False)
            new_loaner.game = game
            new_loaner.save()

            return redirect('board_games:game', game_id=game_id)
    
    # Display a blank or invalid form.
    context = {'game': game, 'form': form}
    return render(request, 'board_games/new_loaner.html', context)

@login_required
def edit_loaner(request, loaner_id):
    """Edit an existing description."""
    loaner = Loaner.objects.get(id=loaner_id)
    game = loaner.game

    if request.method != 'POST':
        # Initial request; pre-fill form with the current description.
        form = LoanerForm(instance=loaner)
    else:
        # POST data submitted; process data.
        form = LoanerForm(instance=loaner, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_games:game', game_id=game.id)
    
    context = {'loaner': loaner, 'game': game, 'form': form}
    return render(request, 'board_games/edit_loaner.html', context)


    #def game_returned(request):
#    instance = Loaner.objects.get(id=id)
#    instance.delete()
#
#    context = {'instance': instance}
#    return render(request, 'board_games/game.html', context)