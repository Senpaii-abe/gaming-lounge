from django.db.models import Q
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User, FriendshipRequest
from account.serializers import UserSerializer
from notification.utils import create_notification

from .best_profanity import has_profanity #profcheck

from .forms import PostForm, AttachmentForm
from .models import Post, Like, Comment, Trend, GameTitle, Category
from .serializers import PostSerializer, PostDetailSerializer, CommentSerializer, TrendSerializer
from account.models import User

@api_view(['GET'])
def post_list(request):
    # Extracting user preferences
    user_pref_titles = request.user.pref_game_titles.split(',') if request.user.pref_game_titles else []
    user_pref_titles = [int(title_id.strip('[]')) for title_id in user_pref_titles if title_id.strip('[]')] if user_pref_titles else []

    user_pref_category = request.user.pref_game_category

    user_ids = [request.user.id]

    for user in request.user.friends.all():
        user_ids.append(user.id)

    # Query for posts based on user preferences
    pref_posts = Post.objects.filter(is_private=False)
    
    if user_pref_titles:
        pref_posts = pref_posts.filter(Q(game_title__id__in=user_pref_titles))
    elif user_pref_category:
        categories = user_pref_category.split(',')
        pref_posts = pref_posts.filter(Q(game_title__categories__game_category__in=categories))

    trend = request.GET.get('trend', '')

    if trend:
        pref_posts = pref_posts.filter(body__icontains='#' + trend)

    # Query for posts from user's friends
    friend_posts = Post.objects.filter(created_by_id__in=user_ids, is_private=False)

    trend = request.GET.get('trend', '')

    if trend:
        friend_posts = friend_posts.filter(body__icontains='#' + trend)

    # Combine the results
    combined_posts = pref_posts | friend_posts

    serializer = PostSerializer(combined_posts, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, pk):
    user_ids = [request.user.id]
    
    for user in request.user.friends.all():
        user_ids.append(user.id)
    
    post = Post.objects.filter(Q(created_by_id__in=user_ids) | Q(is_private=False)).get(pk=pk)
    
    serialized_data = PostDetailSerializer(post).data
    print(serialized_data)  # Check the console for the serialized data
    
    return JsonResponse({
        'post': serialized_data
    })

@api_view(['GET'])
def post_list_profile(request, id):
        
    user = User.objects.get(pk=id) #change later to feed only
    posts = Post.objects.filter(created_by_id = id)
    if not request.user in user.friends.all():
        posts = posts.filter(is_private=False)
    
    
    
    
    post_serializer = PostSerializer(posts, many=True)
    user_serializer = UserSerializer(user)
    
    can_send_friendship_request = True
    
    if request.user in user.friends.all():
        can_send_friendship_request = False
        
    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)
    
    if check1 or check2:
        can_send_friendship_request = False
    
    
    return JsonResponse({
        'posts': post_serializer.data, 
        'user': user_serializer.data,
        'can_send_friendship_request': can_send_friendship_request
    },  safe=False)


@api_view(['POST'])
def post_create(request):
    form = PostForm(request.POST)
    attachment = None
    attachment_form = AttachmentForm(request.POST, request.FILES)
    body = request.data.get("body") #profcheck
    
    print(request.FILES)
    
    if has_profanity(body):  # profcheck
        return Response({"error": "Profanity found"}, status=400)  # profcheck
    
    if attachment_form.is_valid():
        attachment = attachment_form.save(commit=False)
        attachment.created_by = request.user
        attachment.save()
    
    if form.is_valid():
        post = form.save(commit=False) #commit false so it wont go through the backend
        post.created_by = request.user
        post.save()
        
        # Assuming 'game_title' is a valid field in your Post model
        game_title_id = request.POST.get('game_title')
        if game_title_id:
        # Assuming 'game_title' is a ForeignKey field in the Post model
            post.game_title_id = game_title_id
            
        post.save()
            
        if attachment:
            post.attachments.add(attachment)
        

        #to add in post count when user posts
        user = request.user
        user.posts_count = user.posts_count + 1
        user.save()
        
        serializer = PostSerializer(post)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add sumn here later..'})
    
@api_view(['POST'])
def post_like(request, pk):
    post = Post.objects.get(pk=pk)
    
    if not post.likes.filter(created_by=request.user):
        like = Like.objects.create(created_by=request.user)
        
        post = Post.objects.get(pk=pk)
        post.likes_count = post.likes_count + 1
        post.likes.add(like)
        post.save() 
        
        notification = create_notification(request, 'post_like', post_id=post.id)
    
        return JsonResponse({'message': 'like created'})
    else:
        return JsonResponse({'message': 'post already like'})
    
@api_view(['POST'])
def post_create_comment(request, pk):
    
    
    comment = Comment.objects.create(body=request.data.get('body'), created_by=request.user)
    post = Post.objects.get(pk=pk)
    post.comments.add(comment)
    post.comments_count = post.comments_count + 1
    post.save()

    notification = create_notification(request, 'post_comment', post_id=post.id)
    
    serializer = CommentSerializer(comment)
    return JsonResponse(serializer.data, safe=False)


@api_view(['DELETE'])
def post_delete(request, pk):
    # Retrieve the post to be deleted and its creator
    post = Post.objects.filter(created_by=request.user).get(pk=pk)
    user = post.created_by

    # Check if the post exists and if the user is the creator
    if post:
        if user == request.user:
            # Delete the post
            post.delete()
            
            # Update the user's post_count by subtracting 1
            user.posts_count -= 1
            user.save()

            return JsonResponse({'message': 'Post deleted successfully'})
        else:
            return JsonResponse({'error': 'You do not have permission to delete this post'}, status=403)
    else:
        return JsonResponse({'error': 'Post not found'}, status=404)

@api_view(['POST'])
def post_report(request, pk):
    post = Post.objects.get(pk=pk)
    post.reported_by_users.add(request.user)
    post.save()

    return JsonResponse({'message': 'post reported'})

@api_view(['GET'])
def get_trends(request):
    serializer = TrendSerializer(Trend.objects.all(), many=True)
    
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_gametitle(request, *args, **kwargs):
    try:
        # Remove specific fields from the distinct call
        game_titles = GameTitle.objects.values('id', 'title').distinct()
        return JsonResponse(list(game_titles), safe=False)
    except Exception as e:
        print(f"Error in get_gametitle view: {str(e)}")
        return JsonResponse({"error": str(e)}, status=500)

def get_user_post_count(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        post_count = user.posts_count
        return JsonResponse({'posts_count': post_count})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
