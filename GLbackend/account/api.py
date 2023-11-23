from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from notification.utils import create_notification

from .forms import SignupForm, ProfileForm
from .models import User, FriendshipRequest
from .serializers import UserSerializer, FriendshipRequestSerializer
from post.models import GameTitle, Category
import logging

logger = logging.getLogger(__name__)

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
        'avatar': request.user.get_avatar(),
        'pref_game_category': request.user.pref_game_category
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
        user = form.save()
        user.is_active = False
        user.save()

        url = f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'

        #send verification email later
        send_mail(
            "Please verify your email",
            f"The url for activating your account is: {url}",
            "gloungenoreply@gmail.com",
            [user.email],
            fail_silently=False,
        )
    else:
        message = form.errors.as_json()
    
    print(message)

    return JsonResponse({'message': message}, safe=False)


@api_view(['GET']) #receiving friend request
def friends(request, pk):
    user = User.objects.get(pk=pk)
    requests = []

    

    if user == request.user:
        requests = FriendshipRequest.objects.filter(created_for=request.user, status=FriendshipRequest.SENT)
        requests = FriendshipRequestSerializer(requests, many=True)
        requests = requests.data

    #to get all of friends
    friends = user.friends.all()

    return JsonResponse({
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data, 
        'requests': requests
    }, safe=False)
    
    
@api_view(['GET'])
def my_friendship_suggestions(request):
    serializer = UserSerializer(request.user.people_you_may_know, many=True)
    
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def editprofile(request):
    user = request.user
    email = request.data.get('email')

    if User.objects.exclude(id=user.id).filter(email=email).exists(): #to check if email is already used by other user
        return JsonResponse({'message': 'email already exists'})
    else: 

        form = ProfileForm(request.POST, request.FILES, instance=user) #instance - to save it to the user

        if form.is_valid():
            form.save()

        serializer = UserSerializer(user) #set avatar in store when changing avatar

        return JsonResponse({'message': 'information updated', 'user': serializer.data})

@api_view(['POST'])
def editpassword(request):
    user = request.user #logged in user

    form = PasswordChangeForm(data=request.POST, user=user) #request.POST is from the form data

    if form.is_valid():
        form.save()

        return JsonResponse({'message': 'success'})

    else:
        return JsonResponse({'message': form.errors.as_json()}, safe=False)

@api_view(['POST']) #sending friend request
def send_friendship_request(request, pk):
    user = User.objects.get(pk=pk)

    check1 = FriendshipRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendshipRequest.objects.filter(created_for=user).filter(created_by=request.user)
    
    if not check1 or not check2:
        friendrequest = FriendshipRequest.objects.create(created_for=user, created_by=request.user)
        
        notification = create_notification(request, 'new_friendrequest', friendrequest_id=friendrequest.id)

        return JsonResponse({'message': 'friend request created'})
    
    else:
        return JsonResponse({'message': 'request already sent'})
    


@api_view(['POST']) #handle friend request
def handle_request(request, pk, status):
    user = User.objects.get(pk=pk)
    request_user = request.user

    friendship_request = FriendshipRequest.objects.filter(created_for=request_user, created_by=user).first()
    if friendship_request:
        if status == FriendshipRequest.ACCEPTED:
            # Update friendship request status to 'accepted' and delete the request
            friendship_request.status = status
            friendship_request.save()
            friendship_request.delete()

            # Update friends and friends_count for both users
            user.friends.add(request_user)
            user.friends_count = user.friends.count()
            user.save()

            request_user.friends.add(user)
            request_user.friends_count = request_user.friends.count()
            request_user.save()

            return JsonResponse({'message': 'Friend request accepted and updated successfully'}, status=200)
        elif status == FriendshipRequest.REJECTED:
            # Update friendship request status to 'rejected'
            friendship_request.status = status
            friendship_request.save()

            return JsonResponse({'message': 'Friend request rejected'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid status provided'}, status=400)
    else:
        return JsonResponse({'error': 'Friendship request not found'}, status=404)

    notification = create_notification(request, 'accepted_friendrequest', friendrequest_id=friendship_request.id)

@api_view(['POST'])
def update_user_preferences(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse(status=404)

    selected_category = request.data.get('pref_game_category')
    print('Received pref_game_category:', selected_category)  # Add this line for logging
    
    user.pref_game_category = selected_category
    user.save()
    
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def update_user_prefgametitle(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse(status=404)

    selected_titles = request.data.get('pref_game_titles')
    print('Received pref_game_titles:', selected_titles)  # Add this line for logging

    user.pref_game_titles = selected_titles
    user.save()


    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            'id': user.id,
            'name': user.name,
            'pref_game_category': user.pref_game_category,
            # 'game_titles': []  # Add an empty list for game titles
        }

        # Get game titles associated with user's selected categories
        if user.pref_game_category:
            categories = user.pref_game_category.split(',')
            game_titles = GameTitle.objects.filter(categories__game_category__in=categories)
            user_data['game_titles'] = [{'id': title.id, 'title': title.title} for title in game_titles]

        return JsonResponse(user_data)
    except Exception as e:
        logger.exception("Error in get_user view")
        return JsonResponse({'error': str(e)}, status=500)

def get_game_categories(request):
    try:
        categories = Category.objects.values('id', 'game_category')
        return JsonResponse(list(categories), safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    


    
