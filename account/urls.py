from django.urls import path
from .views import register_user, user_login

urlpatterns = [
    path('register/', register_user, name='user-registration'),
    path('login/', user_login, name='user-login'),
    # Add other views as needed
]