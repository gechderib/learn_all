from django.urls import path
from .views import get_all_sub_category,get_sub_category_detail, change_sub_category_detail, addSubCategory, get_all_main_category, get_main_category_detail, addMainCategory,change_category_detail
urlpatterns = [
    path('get-all-category/', get_all_main_category, name='all-category'),
    path('get-one-category/<int:pk>/', get_main_category_detail, name='one-category'),
    path('add-category/', addMainCategory, name='add-category'),
    path('change-category/<int:pk>/', change_category_detail, name='change-category'),
    
    path('get-all-sub-category/', get_all_sub_category, name='all-sub-category'),
    path('get-one-sub-category/<int:pk>/', get_sub_category_detail, name='one-sub-category'),
    path('add-sub-category/', addSubCategory, name='add-sub-category'),
    path('change-sub-category/<int:pk>/', change_sub_category_detail, name='change-sub-category'),
]