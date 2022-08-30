from trading.serializers import BlotterSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from trading.models import Blotter


class BlotterViewSet(generics.ListAPIView):
    """
    A simple ViewSet for listing or retrieving blotters data.
    """
    model = Blotter
    serializer_class = BlotterSerializer
    queryset = Blotter.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'ticker', 'volume', 'price', 'user', 'user__name', 'user__email']
    
   


