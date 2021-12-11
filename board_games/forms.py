from django import forms

from .models import Game, Description, Loaner

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

class LoanerForm(forms.ModelForm):
    class Meta:
        model = Loaner
        fields = ['text']
        labels = {'text': ''}
