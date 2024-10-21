from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    short_description = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Текст')
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.published_date.strftime('%d-%m-%Y %H:%M')

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"