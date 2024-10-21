from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'author', 'published_date')
    search_fields = ('title', 'author__username')
    list_filter = ('published_date', 'author')
    ordering = ('-published_date',)

