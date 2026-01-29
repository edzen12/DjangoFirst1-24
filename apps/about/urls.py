from django.urls import path 
from apps.about.views import aboutFunc, teamsFunc

urlpatterns = [  
    path('', aboutFunc, name='aboutFunc'),
    path('teams/', teamsFunc, name='teamsFunc'),
]
