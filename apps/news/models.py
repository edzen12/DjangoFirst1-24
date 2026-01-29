from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title=models.CharField(
        verbose_name="Название категории", max_length=100)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категория' 


class News(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name="Категория поста", null=True
    )
    title = models.CharField(verbose_name="Заголовок",max_length=100)
    image = models.ImageField(
        upload_to='newsMedia', verbose_name="Фото",
        null=True, blank=True
    )
    description = CKEditor5Field('Описание', config_name='extends')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'
        ordering = ['-id']


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name="Новость", related_name='comments')
    name = models.CharField(verbose_name="ФИО", max_length=50)
    text = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True) # время ставим автоматом
    is_published = models.BooleanField(default=False) # проверяем перед выходом

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'комментарии'