from django.core.exceptions import DisallowedHost
from django.db import models
from django.contrib.auth.models import User #-emilia

# Create your models here.

class Game(models.Model):
    """A board game"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    loaner = ""

    LOAN_STATUS_CHOICES = [
        ('A', 'available'),
        ('U', 'unavailable'),
    ]

    loan_status = models.CharField(max_length=1,choices=LOAN_STATUS_CHOICES,default='A')

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

class Loaner(models.Model):
    """Loaner of a board game"""
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    text = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'loaners'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."