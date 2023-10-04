
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('account.urls')), 
    path('api/posts/', include('post.urls')),
    path('admin/', admin.site.urls),

    # if you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views. uncomment the code below to enable this feature
    #   path('api-auth/', include('rest_framework.urls')) 
]
