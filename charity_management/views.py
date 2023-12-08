# views.py in charity_management app

from rest_framework import generics
from .models import Charity
from .serializers import CharitySerializer

class CharityListView(generics.ListAPIView):
    queryset = Charity.objects.all()
    serializer_class = CharitySerializer
