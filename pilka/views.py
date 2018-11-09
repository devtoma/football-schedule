from django.shortcuts import render
from pilka.forms import AddPlayerForm
from django.views import View
from pilka.models import Player, Game, Series
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView
from pilka.serializers import AddPlayerToGameSerializer
from rest_framework.response import Response
from datetime import datetime
from django.views.generic.list import ListView


# Create your views here.

class MainView(View):

    def get(self, request):
        # player = Player.objects.all()
        form = AddPlayerForm()

        ctx = {
            'form': form
        }
        return render(request, 'add_player.html', ctx)

    def post(self, request):
        form = AddPlayerForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponseRedirect('/')
        else:
            pass


class ListPlayerView(View):
    def get(self, request):
        players = Player.objects.all()
        game = Game.objects.filter(dategame__gte=datetime.now()).order_by('dategame').first()
        players_in_game = game.player.all()
        ctx = {
            'players': players,
            'game': game,
            'players_in_game': players_in_game,
        }
        print(game.dategame)
        return render(request, 'index.html', ctx)


class AddPlayerToGame(APIView):
    def post(self, request):
        # player = request.POST['player.id']
        # game = request.POST['game.id']
        serializer = AddPlayerToGameSerializer(data=request.data)
        if serializer.is_valid():
            # import pdb;pdb.set_trace()
            player_id = serializer.data['playerid']
            game_id = serializer.data['gameid']
            if Series.objects.filter(new_game_id=game_id).count() < 100:
                Series.objects.create(player_id=player_id, new_game_id=game_id)
                return JsonResponse(data=request.data)
            else:
                return Response("Brak możliwości zapisu, na aktualny mecz jest komplet graczy")
        print(serializer.errors)
        return Response(status=400)


class RemoveFromGame(APIView):
    def post(self, request):
        serializer = AddPlayerToGameSerializer(data=request.data)
        if serializer.is_valid():
            player_id = serializer.data['playerid']
            game_id = serializer.data['gameid']
            p = Series.objects.get(player_id=player_id, new_game_id=game_id)
            p.delete()
            return  JsonResponse(data=request.data)


class DetailPlayers(ListView):
    context_object_name = "list_of_players"
    model = Player
    queryset = Player.objects.all().order_by('pk')
    template_name = 'player_list.html'

class DetailGameView(ListView):
    context_object_name = "list_of_games"
    model = Game
    queryset = Game.objects.all().order_by('dategame')
    template_name = 'game_list.html'
