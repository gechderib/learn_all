from django.urls import path
from .views import addCategory, addSubCategory

urlpatterns = [
    path('add-category/', addCategory, name='add-category'),
    path('add-subcategory/', addSubCategory, name='add-subcategory'),
    # Add other views as needed
]