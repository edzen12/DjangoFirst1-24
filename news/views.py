from django.shortcuts import render, get_object_or_404
from news.models import News, Category

def homepage(request):
    news_all = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news_all':news_all,
        'categories':categories,
    }
    return render(request, 'index.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    categories = Category.objects.all()
    context = {
        'news':news,
        'categories':categories,
    }
    return render(request, 'single-page.html', context)