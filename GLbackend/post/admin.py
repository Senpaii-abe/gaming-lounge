from django.contrib import admin

from .models import Post, PostAttachments

admin.site.register(Post)
admin.site.register(PostAttachments)
