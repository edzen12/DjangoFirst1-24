from django.contrib import admin
from news.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    prepopulated_fields = {'slug': ['title']}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)