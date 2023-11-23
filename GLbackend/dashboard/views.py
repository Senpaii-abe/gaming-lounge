from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from account.models import User
from post.models import Post

from django.db.models import Count
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from account.forms import ProfileEditForm, ChangePasswordForm
# Create your views here.

    
@login_required
def dashboard(request):

    admin = request.user
    # Total users count
    total_users_count = User.objects.count()

    # Total posts count
    total_posts_count = Post.objects.count()

    # Calculate the date one week ago from today
    one_week_ago = timezone.now() - timedelta(days=7)
    # Count posts created within the last week
    posts_count_week = Post.objects.filter(created_at__gte=one_week_ago).count()
    users_count_week = User.objects.filter(date_joined__gte=one_week_ago).count()


    
    #GRAPH - PER MONTH

    # specific_month = 11  # November
    # specific_year = 2023  # Specify the year as needed

    # # Get the number of days in the specific month
    # num_days_in_month = 30  # Assuming November has 30 days

    # # Create a list to store the counts for each day in November
    # user_counts_per_day = []
    # post_counts_per_day = []

    # # Loop through each day of the month and get counts for users and posts
    # for day in range(1, num_days_in_month + 1):
    #     start_date = datetime(specific_year, specific_month, day)
    #     end_date = start_date + timedelta(days=1)

    #     # Get count of users joined on this day
    #     users_count = User.objects.filter(date_joined__gte=start_date, date_joined__lt=end_date).count()
    #     user_counts_per_day.append(users_count)

    #     # Get count of posts created on this day
    #     posts_count = Post.objects.filter(created_at__gte=start_date, created_at__lt=end_date).count()
    #     post_counts_per_day.append(posts_count)

    # Combine both sets of data into one context dictionary
    context = {
        'admin_name': admin.name,
        'admin_email': admin.email,
        'admin_avatar' : admin.avatar,
        'total_users_count': total_users_count,
        'total_posts_count': total_posts_count,
        'posts_count_week': posts_count_week,
        'users_count_week': users_count_week,
        # 'user_counts_per_day': user_counts_per_day,
        # 'post_counts_per_day': post_counts_per_day,
    }

    return render(request, 'admin/index.html', context)


def get_chart_data(request):
    chart_type = request.GET.get('chartType', 'weekly')
    print(f"Chart Type: {chart_type}")

    # Initialize default response data
    data = {'error': 'An error occurred while fetching data'}

    if chart_type == 'weekly':
        # Initialize lists to store daily counts for the week
        labels_weekly = []
        user_counts_weekly = []
        post_counts_weekly = []

        # Calculate the date one week ago from today
        start_date_weekly = timezone.now() - timedelta(days=6)  # Start from a week ago
        end_date_weekly = timezone.now()  # Today

        
# Query to get daily counts of posts within the week
        daily_data_posts_weekly = Post.objects.filter(created_at__range=(start_date_weekly, end_date_weekly)) \
            .extra({'created_day': "strftime('%%Y-%%m-%%d', created_at)"}) \
            .values('created_day') \
            .annotate(posts=Count('id'))

        # Populate labels_weekly and post_counts_weekly
        for entry in daily_data_posts_weekly:
            labels_weekly.append(entry['created_day'])  # No need for strftime for this format
            post_counts_weekly.append(entry['posts'])

        # Query to get daily counts of users within the week
        daily_data_users_weekly = User.objects.filter(date_joined__range=(start_date_weekly, end_date_weekly)) \
            .extra({'date_joined_day': "strftime('%%Y-%%m-%%d', date_joined)"})  \
            .values('date_joined_day') \
            .annotate(users=Count('id'))

        # Populate user_counts_weekly
        for entry in daily_data_users_weekly:
            user_counts_weekly.append(entry['users'])

        # Create data dictionary for the weekly timeframe
        weekly_data = {
            'labels': labels_weekly,
            'userCounts': user_counts_weekly,
            'postCounts': post_counts_weekly
        }

        data = weekly_data

    elif chart_type == 'monthly':
        # Initialize lists to store daily counts for the month of November
        labels_monthly = []
        user_counts_monthly = []
        post_counts_monthly = []

        # Calculate the start and end of November
        start_date_monthly = timezone.make_aware(datetime(datetime.now().year, 11, 1))
        end_date_monthly = timezone.make_aware(datetime(datetime.now().year, 11, 30, 23, 59, 59))

        # Query to get daily counts of posts and users within November
        daily_data_posts_monthly = Post.objects.filter(created_at__range=(start_date_monthly, end_date_monthly)) \
            .extra({'created_day': 'date(created_at)'}) \
            .values('created_day') \
            .annotate(posts=Count('id'))

        for entry in daily_data_posts_monthly:
            labels_monthly.append(entry['created_day'].strftime('%Y-%m-%d'))
            post_counts_monthly.append(entry['posts'])

        daily_data_users_monthly = User.objects.filter(date_joined__range=(start_date_monthly, end_date_monthly)) \
            .extra({'date_joined_day': 'date(date_joined)'}) \
            .values('date_joined_day') \
            .annotate(users=Count('id'))

        for entry in daily_data_users_monthly:
            user_counts_monthly.append(entry['users'])

        # Create data dictionary for the monthly timeframe
        monthly_data = {
            'labels': labels_monthly,
            'userCounts': user_counts_monthly,
            'postCounts': post_counts_monthly
        }

        data = monthly_data

    else:
        return JsonResponse({'error': 'Invalid chart type'})

    print(f"Final Data: {data}")
    return JsonResponse(data)


#EDIT ADMIN
@login_required
def edit_profile(request):

    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
    
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    else:

        profile_form = ProfileEditForm(instance=request.user)
        print(profile_form.errors)  # Check form errors in the console

    return render(request, 'admin/edit_profile.html', {'profile_form': profile_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            # Retrieve the new password from the form
            new_password = form.cleaned_data['new_password']
            
            # Update the logged-in admin's password
            request.user.set_password(new_password)
            request.user.save()
            
            # Keep the user logged in after password change
            update_session_auth_hash(request, request.user)
            
            # Add a success message
            messages.success(request, 'Your password has been successfully changed!')
            
            # Redirect to the 'editprofile/' page
            return redirect('edit_profile')
    else:
        form = ChangePasswordForm(user=request.user) # Pass the user to the form
    
    return render(request, 'admin/change_password.html', {'form': form})