from rest_framework import viewsets
from .models import Client, Keyword, RankResult
from .serializers import ClientSerializer, KeywordSerializer, RankResultSerializer

class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_fields = ['name']

class KeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    filterset_fields = ['name', 'clients']

class RankResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RankResult.objects.all()
    serializer_class = RankResultSerializer
    filterset_fields = ['keyword', 'domain', 'position', 'checked_at']