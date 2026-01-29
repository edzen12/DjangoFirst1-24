from django.urls import path
from apps.news.views import homepage, news_detail, category_detail

urlpatterns = [ 
    path('', homepage, name='homepage'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
]
