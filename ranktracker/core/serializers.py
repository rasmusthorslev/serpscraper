from rest_framework import serializers
from .models import Client, Keyword, RankResult

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class KeywordSerializer(serializers.ModelSerializer):
    clients = ClientSerializer(many=True, read_only=True)
    class Meta:
        model = Keyword
        fields = '__all__'

class RankResultSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer(read_only=True)
    class Meta:
        model = RankResult
        fields = '__all__'