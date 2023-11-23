from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .models import Post

def admin_posts(request):
    admin=request.user

    total_posts_count = Post.objects.count()

    context = {
        'admin_name': admin.name,
        'admin_email': admin.email,
        'admin_avatar' : admin.avatar,
        'total_posts_count' : total_posts_count,
    }
    return render(request, 'admin/posts.html', context)


def reported_posts(request):
    admin=request.user

    context = {
        'admin_name': admin.name,
        'admin_email': admin.email,
        'admin_avatar' : admin.avatar,
    }
    return render(request, 'admin/reported_posts.html', context)