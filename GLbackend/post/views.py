from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .best_profanity import has_profanity #profcheck
from .models import Post, GameTitle
from .forms import PostForm, EditPostForm
from rest_framework.response import Response #profcheck


import uuid

def admin_posts(request):
    admin=request.user

    posts = Post.objects.all()

    total_posts_count = Post.objects.count()
    discussion_posts = Post.objects.filter(menu='Discussions').count()
    tournament_posts = Post.objects.filter(menu='Tournament').count()
    connect_posts = Post.objects.filter(menu='Connect').count()
    marketplace_posts = Post.objects.filter(menu='Marketplace').count()
    beta_posts = Post.objects.filter(menu='Beta').count()

    context = {
        'admin_name': admin.name,
        'admin_email': admin.email,
        'admin_avatar' : admin.avatar,
        'total_posts_count' : total_posts_count,
        'discussion_posts' : discussion_posts,
        'tournament_posts' : tournament_posts,
        'connect_posts' : connect_posts,
        'marketplace_posts' : marketplace_posts,
        'beta_posts': beta_posts,
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

def delete_selected_posts(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids[]')  # Retrieve selected IDs
        
        # Validate selected IDs as UUIDs
        try:
            uuids = [uuid.UUID(id_) for id_ in selected_ids]
        except ValueError:
            return JsonResponse({'message': 'Invalid UUID format in selected IDs'}, status=400)
        
        # If the IDs are valid UUIDs, proceed with deletion
        posts_to_delete = Post.objects.filter(id__in=uuids)
        posts_to_delete.delete()
        return JsonResponse({'message': 'Selected posts deleted successfully'}, status=200)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

def reported_posts(request):
    admin=request.user

    context = {
        'admin_name': admin.name,
        'admin_email': admin.email,
        'admin_avatar' : admin.avatar,
    }
    return render(request, 'admin/reported_posts.html', context)

#profcheck
def post_create(request):
    body = request.data.get("body")

    if has_profanity(body):
        return Response({"error": "Profanity found"}, status=400)
