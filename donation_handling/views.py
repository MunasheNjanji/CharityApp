# views.py in donation_handling app

from rest_framework import generics
from .models import Donation
from .serializers import DonationSerializer

class DonationHistoryView(generics.ListAPIView):
    serializer_class = DonationSerializer

    def get_queryset(self):
        user = self.request.user
        return Donation.objects.filter(donor=user)


class DonationCreateView(generics.CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class DonationUpdateView(generics.UpdateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class DonationDeleteView(generics.DestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer


class DonationListView(generics.ListAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
