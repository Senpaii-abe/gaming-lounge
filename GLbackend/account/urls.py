from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

from . import api

urlpatterns = [
    path('me/', api.me,name='me'),
    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'), 
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('editprofile/', api.editprofile, name='editprofile'),
    path('editpassword/', api.editpassword, name='editpassword'),
    path('friends/suggested/', api.my_friendship_suggestions, name='my_friendship_suggestions'),
    path('friends/<uuid:pk>/', api.friends, name='friends'),
    path('friends/<uuid:pk>/request/', api.send_friendship_request, name='send_friendship_request'),
    path('friends/<uuid:pk>/<str:status>/', api.handle_request, name='handle_request'),
    path('update_user_preferences/<uuid:user_id>/', api.update_user_preferences, name='update_user_preferences'),
    path('update_user_prefgametitle/<uuid:user_id>/', api.update_user_prefgametitle, name='update_user_prefgametitle'),
    path('get_game_categories/', api.get_game_categories, name='get_game_categories'),
    path('get_user/<uuid:user_id>/', api.get_user, name='get_user'),
]