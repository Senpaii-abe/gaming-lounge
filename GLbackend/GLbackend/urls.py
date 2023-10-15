from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from account.views import activateemail

urlpatterns = [
    path('api/', include('account.urls')), 
    path('api/posts/', include('post.urls')),
    path('api/search/', include('search.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/notifications/', include('notification.urls')),
    path('activateemail/', activateemail, name='activateemail'),
    path('admin/', admin.site.urls),

    # if you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. uncomment the code below to enable this feature
    #   path('api-auth/', include('rest_framework.urls')) 
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
