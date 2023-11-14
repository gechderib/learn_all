from django.urls import path
from .views import register_user, user_login, user_logout

urlpatterns = [
    path('register/', register_user, name='user-registration'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout')
    # Add other views as needed
]