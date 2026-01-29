from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category, Comment
from news.forms import CommentForm


def homepage(request):
    news_all = News.objects.all()
    categories = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'news_all':news_all,
        'categories':categories,
    }
    return render(request, 'index.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    categories = Category.objects.filter(news__isnull=False).distinct()
    comments = news.comments.filter(is_published=True).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news 
            comment.save()
            return redirect('news_detail', slug=slug)
    else:
        form = CommentForm()
    context = {
        'news':news,
        'comments':comments,
        'categories':categories,
        'form':form
    }
    return render(request, 'single-page.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news = News.objects.filter(category=category)
    categories = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'news':news,
        'category':category,
        'categories':categories,
    }
    return render(request, 'category-detail.html', context)