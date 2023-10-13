from django.http import HttpResponse
from django.shortcuts import render

from .models import User

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