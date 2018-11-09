from rest_framework import serializers

class AddPlayerToGameSerializer(serializers.Serializer):
    playerid = serializers.IntegerField()
    gameid = serializers.IntegerField()