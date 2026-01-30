from django.urls import path 
from apps.about.views import aboutFunc, teamsFunc, team_detail

urlpatterns = [  
    path('', aboutFunc, name='aboutFunc'),
    path('teams/', teamsFunc, name='teamsFunc'),
    path('teams/<slug:slug>/', team_detail, name='team_detail'),
]
