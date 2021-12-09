from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Board Games."""
    return render(request, 'board_games/index.html')