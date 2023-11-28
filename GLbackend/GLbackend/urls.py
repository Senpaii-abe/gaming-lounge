from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from dashboard import views
from account import views
from django.urls import include, path


urlpatterns = (
    [
        # path("__debug__/", include("debug_toolbar.urls")),
        path("api/", include("account.urls")),
        path("api/posts/", include("post.urls")),
        path("api/search/", include("search.urls")),
        path("api/chat/", include("chat.urls")),
        path("api/notifications/", include("notification.urls")),
        path("activateemail/", views.activateemail, name="activateemail"),
        # admin
        path("admin/", include("account.urls")),
        path("admin/", include("dashboard.urls")),
        path("admin/", include("post.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
