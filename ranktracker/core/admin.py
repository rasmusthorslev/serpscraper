from django.contrib import admin
from .models import Client, Keyword, RankResult

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Show the name field in the admin list

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'get_clients')
    list_filter = ('name','clients')

    def get_clients(self, obj):
        return ", ".join([c.name for c in obj.clients.all()])
    get_clients.short_description = 'clients'

@admin.register(RankResult)
class RankResultAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'domain', 'position', 'checked_at')  # Optionally show client
    list_filter = ('keyword', 'domain')