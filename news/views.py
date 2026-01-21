from django.shortcuts import render
from news.models import News

def homepage(request):
    news_all = News.objects.all()
    context = {
        'news_all':news_all,
    }
    return render(request, 'index.html', context)
