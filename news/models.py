from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'
        ordering = ['-id']
