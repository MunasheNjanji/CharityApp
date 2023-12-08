# views.py in campaign_management app

from rest_framework import generics
from .models import Campaign
from .serializers import CampaignSerializer
# import timezone
from django.utils import timezone

class OngoingCampaignListView(generics.ListAPIView):
    queryset = Campaign.objects.filter(end_date__gte=timezone.now(), goal_amount__gt=F('current_amount'))
    serializer_class = CampaignSerializer

class CampaignDetailView(generics.RetrieveAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignCreateView(generics.CreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignUpdateView(generics.UpdateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignDeleteView(generics.DestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignListView(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignUpdateView(generics.UpdateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignDeleteView(generics.DestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaignListView(generics.ListAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
