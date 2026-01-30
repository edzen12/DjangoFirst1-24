from django.shortcuts import render, get_object_or_404
from apps.about.models import About, Team
from apps.news.models import Category


def aboutFunc(request):
    about = About.objects.latest('-id')
    categories = Category.objects.filter(news__isnull=False).distinct()
    context = { 
        'categories':categories,
        'about':about
    }
    return render(request, 'pages/about.html', context)


def teamsFunc(request):
    teams = Team.objects.prefetch_related('sociallink_set')
    categories = Category.objects.filter(news__isnull=False).distinct()
    context = { 
        'categories':categories,
        'teams':teams
    }
    return render(request, 'pages/teams.html', context)



def team_detail(request, slug):
    team = get_object_or_404(Team, slug=slug)
    categories = Category.objects.filter(news__isnull=False).distinct()  
    context = {
        'team':team, 
        'categories':categories 
    }
    return render(request, 'pages/team-single.html', context)
