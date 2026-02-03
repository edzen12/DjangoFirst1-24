from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from apps.news.models import News, Category
from apps.news.forms import CommentForm


def homepage(request):
    news_all = News.objects.all()
    categories = Category.objects.filter(news__isnull=False).distinct()

    paginator = Paginator(news_all, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj,
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
    return render(request, 'pages/single-page.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news = News.objects.filter(category=category)
    categories = Category.objects.filter(news__isnull=False).distinct()
    context = {
        'news':news,
        'category':category,
        'categories':categories,
    }
    return render(request, 'pages/category-detail.html', context)