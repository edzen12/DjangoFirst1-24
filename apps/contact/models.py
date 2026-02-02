from django.db import models


class Contact(models.Model):
    title = models.CharField(verbose_name="Название страницы", max_length=40)
    phone_number1=models.CharField(
        verbose_name="Номер телефона №1", max_length=20, help_text="+996 707 555 444"
    )
    phone_number2=models.CharField(
        verbose_name="Номер телефона №2", max_length=20, blank=True, 
        null=True, help_text="+996 507 555 444"
    )
    phone_number3=models.CharField(
        verbose_name="Номер телефона №3", max_length=20, blank=True, 
        null=True, help_text="+996 222 555 444"
    )
    map = models.TextField(verbose_name="Ссылка на карту")
    time_to_work = models.CharField(
        max_length=100, verbose_name="Время работы",blank=True, 
        null=True, help_text='c 08:00 до 17:00'
    )
    social_instagram = models.CharField(
        verbose_name="Ссылка на instagram", max_length=255, blank=True, 
        null=True, help_text="https://www.instagram.com/edzen_bey/"
    )
    social_telegram = models.CharField(
        verbose_name="Ссылка на telegram", max_length=255, blank=True, 
        null=True, help_text="https://t.me/edzenDev"
    )
    social_whatsapp = models.CharField(
        verbose_name="Ссылка на instagram", max_length=255, blank=True, 
        null=True, help_text="https://wa.me/996703016683/"
    )
    social_facebook = models.CharField(
        verbose_name="Ссылка на facebook", max_length=255, blank=True, 
        null=True, help_text="https://www.facebook.com/groups/feed/"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'контакт'
