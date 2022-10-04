"""
Views for the user API.
"""
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializers import (
    UserSerializer,
    UserTokenObtainPairSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class UserTokenObtainPairView(TokenObtainPairView):
    """Create refresh and access token."""
    serializer_class = UserTokenObtainPairSerializer


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
