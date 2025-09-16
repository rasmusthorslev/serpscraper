from django.contrib import admin
from .models import Keyword, RankResult

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

@admin.register(RankResult)
class RankResultAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'domain', 'position', 'checked_at')
    list_filter = ('keyword', 'domain')