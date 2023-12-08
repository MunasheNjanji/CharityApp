# views.py in analytics_reporting app

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Donation

class GlobalStatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        total_funds_raised = Donation.objects.aggregate(Sum('amount'))['amount__sum']
        total_donations = Donation.objects.count()
        
        return Response({
            'total_funds_raised': total_funds_raised,
            'total_donations': total_donations,
        })


class CharityStatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        charity_id = kwargs['pk']
        total_funds_raised = Donation.objects.filter(charity_id=charity_id).aggregate(Sum('amount'))['amount__sum']
        total_donations = Donation.objects.filter(charity_id=charity_id).count()
        
        return Response({
            'total_funds_raised': total_funds_raised,
            'total_donations': total_donations,
        })


class UserStatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        total_funds_raised = Donation.objects.filter(donor_id=user_id).aggregate(Sum('amount'))['amount__sum']
        total_donations = Donation.objects.filter(donor_id=user_id).count()
        
        return Response({
            'total_funds_raised': total_funds_raised,
            'total_donations': total_donations,
        })


class CampaignStatisticsView(APIView):
    def get(self, request, *args, **kwargs):
        campaign_id = kwargs['pk']
        total_funds_raised = Donation.objects.filter(campaign_id=campaign_id).aggregate(Sum('amount'))['amount__sum']
        total_donations = Donation.objects.filter(campaign_id=campaign_id).count()
        
        return Response({
            'total_funds_raised': total_funds_raised,
            'total_donations': total_donations,
        })

