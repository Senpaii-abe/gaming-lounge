from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

from . import api

urlpatterns = [
    path('signup/', api.signup, name='signup'),
    path('/', TokenObtainPairView.as_view(), name='token_obtain'), #changed from login/ to just / based on index.js -joey
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]