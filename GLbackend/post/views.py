from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, GameTitle
from .forms import PostForm, EditPostForm

def admin_posts(request):
    admin=request.user

    posts = Post.objects.all()

    total_posts_count = Post.objects.count()
    discussion_posts = Post.objects.filter(menu=Post.DISCUSSION).count()
    tournament_posts = Post.objects.filter(menu=Post.TOURNAMENT).count()
    connect_posts = Post.objects.filter(menu=Post.CONNECT).count()
    marketplace_posts = Post.objects.filter(menu=Post.MARKETPLACE).count()

    context = {
        'admin_name': admin.name,
        'admin_email': admin.email,
        'admin_avatar' : admin.avatar,
        'total_posts_count' : total_posts_count,
        'discussion_posts' : discussion_posts,
        'tournament_posts' : tournament_posts,
        'connect_posts' : connect_posts,
        'marketplace_posts' : marketplace_posts,
        'posts': posts
    }
    return render(request, 'admin/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.created_by = request.user
            new_post.save()
            return redirect('admin_posts')
    else:
        form = PostForm()
        form.fields['game_title'].queryset = GameTitle.objects.all()  # Set the queryset for game_title field

    return render(request, 'admin/add_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('admin_posts')  # Redirect to the admin posts page after editing
    else:
        form = EditPostForm(instance=post)
    
    return render(request, 'admin/edit_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('admin_posts')  # You can return a response or redirect as needed

def reported_posts(request):
    admin=request.user

    context = {
        'admin_name': admin.name,
        'admin_email': admin.email,
        'admin_avatar' : admin.avatar,
    }
    return render(request, 'admin/reported_posts.html', context)