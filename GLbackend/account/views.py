from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404

from .models import User

@require_GET
def get_user(request, user_id):
    try:
        user = request.user
        # Customize the fields you want to include in the response
        user_data = {
            'id': user.id,
            'name': user.name,
            'pref_game_category': user.pref_game_category,
            # Add other fields as needed
        }
        return JsonResponse(user_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Create your views here (not in the front end)
def activateemail(request):
    email = request.GET.get('email', '')
    id = request.GET.get('id', '')

    if email and id:
        user = User.objects.get(id=id, email=email)
        user.is_active = True
        user.save()
    
        return HttpResponse('the user is now activated. You can now log in.')
    
    else:
        return HttpResponse('The parameters is not valid')
