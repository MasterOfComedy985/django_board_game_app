from django import forms

from .models import Game, Description

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['text']
        labels = {'text': ''}

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
