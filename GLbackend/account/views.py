from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .forms import adminForm, SignupForm, UserEditForm

from .models import User, UserVisit


@require_GET
def get_user(request, user_id):
    try:
        user = request.user
        # Customize the fields you want to include in the response
        user_data = {
            "id": user.id,
            "name": user.name,
            "pref_game_category": user.pref_game_category,
            # Add other fields as needed
        }
        return JsonResponse(user_data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Create your views here (not in the front end)
def activateemail(request):
    email = request.GET.get("email", "")
    id = request.GET.get("id", "")

    if email and id:
        user = User.objects.get(id=id, email=email)
        user.is_active = True
        user.save()

        return HttpResponse("the user is now activated. You can now log in.")

    else:
        return HttpResponse("The parameters is not valid")


# ADMIN
def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect("dashboard")  # Redirect to the dashboard or another page
        else:
            messages.error(
                request, "Invalid email or password. Please try again."
            )  # Add an error message
            return render(
                request, "admin/login.html", {"email": email}
            )  # Pass email to the template context for prefilling the form

    return render(request, "admin/login.html")


def admin_signup(request):
    if request.method == "POST":
        form = adminForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_staff = True  # Set the user as staff/admin
            new_user.save()
            return redirect(
                "admin_login"
            )  # Redirect to the login page after successful signup
    else:
        form = adminForm()

    return render(request, "admin/signup.html", {"form": form})


# USER PAGE FOR ADMIN
def admin_users(request):
    admin = request.user

    total_users_count = User.objects.count()

    # Get the current time in the current timezone
    current_time = timezone.now()

    # Set the start and end dates for November with timezone information
    start_date = timezone.datetime(current_time.year, 11, 1, tzinfo=timezone.utc)
    end_date = timezone.datetime(current_time.year, 12, 1, tzinfo=timezone.utc)

    active_users_november_count = User.objects.filter(is_active=True).count()

    # Retrieve new users in November
    new_users_november = User.objects.filter(
        date_joined__gte=start_date, date_joined__lt=end_date
    ).count()

    # BAR GRAPH - USER VISITS
    # Query and count unique visits for each page
    discussion_visits = UserVisit.objects.filter(
        visited_page__contains="post_list"
    ).count()
    connect_visits = UserVisit.objects.filter(
        visited_page__contains="connect_posts"
    ).count()
    marketplace_visits = UserVisit.objects.filter(
        visited_page__contains="marketplace_posts"
    ).count()
    tournament_visits = UserVisit.objects.filter(
        visited_page__contains="tournament_posts"
    ).count()
    beta_testing_visits = UserVisit.objects.filter(
        visited_page__contains="beta_posts"
    ).count()

    # table
    users = User.objects.all()

    context = {
        "admin_name": admin.name,
        "admin_email": admin.email,
        "admin_avatar": admin.avatar,
        "total_users_count": total_users_count,
        "active_users_november_count": active_users_november_count,
        "new_users_november": new_users_november,
        "users": users,
        "discussion_visits": discussion_visits,
        "connect_visits": connect_visits,
        "marketplace_visits": marketplace_visits,
        "tournament_visits": tournament_visits,
        "beta_testing_visits": beta_testing_visits,
    }
    return render(request, "admin/users.html", context)


def add_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_users")
    else:
        form = SignupForm()

    return render(request, "admin/add_user.html", {"form": form})


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(
                "admin_users"
            )  # Redirect to user list page or wherever needed
    else:
        form = UserEditForm(instance=user)

    return render(request, "admin/edit_user.html", {"form": form, "user": user})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect("admin_users")  # You can return a response or redirect as needed
