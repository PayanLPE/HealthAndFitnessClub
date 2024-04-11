from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('login/', views.sign_in, name='sign_in'),
    path('logout/', views.sign_out, name='sign_out'),
    path('register/', views.register, name='register'),
    path('members/<int:id>/', views.member_dashboard, name='members'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('my_profile/update_info', views.update_info, name='update_info'),
    path('my_profile/add_goal', views.add_goal, name='add_goal'),
    path('my_profile/edit_goal', views.edit_goal, name='edit_goal'),
    path('my_profile/delete_goal', views.delete_goal, name='delete_goal'),
]