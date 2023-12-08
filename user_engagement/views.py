# views.py in user_management app

from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer

class UserProfileView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer

    # Add your code here
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        # Perform any additional operations with the user object
        # ...
        
        return self.retrieve(request, *args, **kwargs)
