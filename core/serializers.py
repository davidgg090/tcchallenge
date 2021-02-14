from django.db.models import fields
from rest_framework import serializers
from .models import Scraper, Asset, AssetData


class ScraperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scraper
        fields = '__all__'


class AssetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetData
        fields = [
            'price',
            'low_24h',
            'high_24h',
            'retunrs_24h',
            'retunrs_ytd',
            'volatility']


class AssetListSerializer(serializers.ModelSerializer):
    values = AssetDataSerializer(
        source="assetdata_set",
        many=True,
        read_only=True)

    class Meta:
        model = Asset
        fields = ['name', 'values']


class AssetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['name', 'description']
