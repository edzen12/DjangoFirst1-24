from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class About(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="О нас",
        help_text='О нас / О компании / История'
    )
    description = CKEditor5Field('Описание', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'О нас'


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    exp = models.CharField(max_length=100, verbose_name="Опыт")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Сотрудники'

class SocialLink(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Сотрудник")
    title = models.CharField(verbose_name="Название соцсети", max_length=100)
    link = models.CharField(verbose_name="Ссылка на аккаунт", max_length=255)

    def __str__(self):
        return self.title
    