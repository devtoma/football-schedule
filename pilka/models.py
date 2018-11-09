from django.db import models


# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=42, blank=True)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=127, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    def isInGame(self, game):
        return self in game.player.all()

class Account(models.Model):
    payment = models.DecimalField(max_digits=7, decimal_places=2)
    saldo = models.DecimalField(max_digits=7, decimal_places=2)

class Game(models.Model):
    dategame = models.DateTimeField()
    place = models.CharField(max_length=127, default='Skra')
    player = models.ManyToManyField(Player, through='Series')
    game_price = models.DecimalField(max_digits=7, decimal_places=2, default='220')

    def __str__(self):
        return self.dategame.strftime("%d/%m/%Y")

class Series(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    new_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    #data = models.DateTimeField()


