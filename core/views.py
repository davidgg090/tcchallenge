from django.db.models import query
from rest_framework import generics
from core.models import Scraper, Asset
from core.serializers import ScraperSerializer, AssetListSerializer, AssetDetailSerializer
from rest_framework.response import Response
from core.task import get_info_scraper
from rest_framework import viewsets


class ScraperViewSet(viewsets.ModelViewSet):
    """
    A model viewset for viewing and editing scraper instances.
    """
    serializer_class = ScraperSerializer
    queryset = Scraper.objects.all()

    def list(self, request):
        queryset = Scraper.objects.all()
        serializer = ScraperSerializer(queryset, many=True)
        get_info_scraper()
        return Response(serializer.data)


class AssetListAPIView(generics.ListAPIView):
    """
    A list view for asset instances.
    """
    serializer_class = AssetListSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        name = name.upper()
        return Asset.objects.filter(name=name)
