from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class News(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='newsMedia', null=True, blank=True)
    description = CKEditor5Field('Text', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'новость'
        ordering = ['-id']
