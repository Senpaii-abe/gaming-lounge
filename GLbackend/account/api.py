from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'name': data.get('name'),
        'email': data.get('email'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()

        #send verification email later
    else:
        message = 'error'

    return JsonResponse({'message': message})


@api_view(['GET']) #receiving friend request
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []

    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    #to get all of friends
    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data, 
        'requests': requests
    }, safe=False)

@api_view(['POST']) #sending friend request
def send_friendship_request(request, pk):
    user = User.objects.get(pk=pk)

    friendship_request = FriendshipRequest(created_for=user, created_by=request.user)


    return JsonResponse({'message': 'friend request created'})