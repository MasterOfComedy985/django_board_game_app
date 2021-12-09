from django.core.exceptions import DisallowedHost
from django.db import models

# Create your models here.

class Game(models.Model):
    """A board game"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Description(models.Model):
    """Description of a board game"""
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'descriptions'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."