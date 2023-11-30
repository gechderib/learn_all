from django.urls import path
from .views import register_user, register_admin, user_login, user_logout,get_all_users

urlpatterns = [
    path('register/', register_user, name='user-registration'),
    path('register_admin/', register_admin, name='user-admin'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('users/',get_all_users,name='all-users')
    # Add other views as needed
] 
