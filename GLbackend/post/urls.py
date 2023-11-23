from django.urls import path

from . import api, views

urlpatterns = [
    path('', api.post_list, name='post_list'),
    path('<uuid:pk>/', api.post_detail, name='post_detail'),
    path('<uuid:pk>/like/', api.post_like, name='post_like'),
    # path('<uuid:pk>/unlike/', api.post_unlike, name='post_unlike'),
    path('<uuid:pk>/comment/', api.post_create_comment, name='post_create_comment'),
    path('<uuid:pk>/delete/', api.post_delete, name='post_delete'),
    path('<uuid:pk>/report/', api.post_report, name='post_report'),
    path('profile/<uuid:id>/', api.post_list_profile, name='post_list_profile'),
    path('create/', api.post_create, name='post_create'),
    path('trends/', api.get_trends, name='get_trends'),
    path('get_gametitle/', api.get_gametitle, name='get_gametitle'),
    # path('delete_post/', api.delete_post, name='delete_post'),
    path('api/users/<uuid:user_id>/post_count/', api.get_user_post_count, name='user_post_count'),

    #admin
    path('gl-posts/', views.admin_posts, name='admin_posts'),
    path('gl-posts/add', views.add_post, name='add_post'),
    path('gl-posts/edit/<uuid:post_id>/', views.edit_post, name='edit_post'),
    path('gl-posts/delete/<uuid:post_id>/', views.delete_post, name='delete_post'),
    path('gl-posts/reported', views.reported_posts, name='reported_posts'),
]