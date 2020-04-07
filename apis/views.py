from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import Team,Player
from .serializers import TeamSerializer,PlayerSerializer

@api_view(['GET','POST'])
def team_list(request):

    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams,many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT'])        
def get_update_team(request,pk):
    
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TeamSerializer(team,data = request.data)
        
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def player_list(request,pk):
    
    if request.method == "GET":
       
        players = Player.objects.filter(team__id=pk)
        
        serializer = PlayerSerializer(players,many=True)
        
        return Response(serializer.data)
    elif request.method =="POST":
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def get_player_update_delete(request,pk,pk_alt):
    
    try:
            player = Player.objects.filter(team__id=pk,id=pk_alt)
    except Player.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
        
    if request.method == 'GET':
        
        serializer = PlayerSerializer(player,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
       
        serializer = PlayerSerializer(player,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
           
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        