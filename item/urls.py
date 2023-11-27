from django.urls import path
from .views import get_all_item, add_item

urlpatterns = [
    path('items/', get_all_item, name='item-list'),
    path('add-item/', add_item, name='item-list'),
]
