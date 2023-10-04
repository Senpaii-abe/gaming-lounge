from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all() #change later to feed only
    
    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def post_list_profile(request, id):
    posts = Post.objects.filter(created_by_id = id)
    
    serializer = PostSerializer(posts, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def post_create(request):
    form = PostForm(request.data)
    
    if form.is_valid():
        post = form.save(commit=False) #commit false so it wont go through the backend
        post.created_by = request.user
        post.save()
        
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add sumn here later..'})
    