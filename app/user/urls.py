"""
URL mappings for the user API.
"""
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path(
        'token/',
        views.UserTokenObtainPairView.as_view(),
        name='token'
    ),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
