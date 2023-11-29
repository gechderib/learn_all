from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import register_user, register_admin, user_login, user_logout

urlpatterns = [
    path('register/', register_user, name='user-registration'),
    path('register_admin/', register_admin, name='user-admin'),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout')
    # Add other views as needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
