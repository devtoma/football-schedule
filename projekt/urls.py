"""projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pilka.views import MainView, ListPlayerView, AddPlayerToGame, DetailPlayers, RemoveFromGame, DetailGameView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="add-player"),
    path('players/', ListPlayerView.as_view(), name="main"),
    path('addtogame/', AddPlayerToGame.as_view()),
    path('listofplayers/', DetailPlayers.as_view(), name="list-player"),
    path('removeplayer/', RemoveFromGame.as_view(), name="remove-player"),
    path('gamelist/', DetailGameView.as_view(), name="game-list")


]
