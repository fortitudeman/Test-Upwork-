from django.urls import path,include,re_path
from .views import team_list,get_update_team,player_list,get_player_update_delete

urlpatterns = [
    path('team/',team_list,name="team-list"),
    path('team/<pk>/',get_update_team,name="team"),
    path('team/<pk>/player/',player_list,name="player-list"),
    path('team/<pk>/player/<pk_alt>/',get_player_update_delete,name="player")
]