from django.urls import path
from .views import get_all_items,add_item, get_one_item, update_item

urlpatterns = [
    path('items/', get_all_items, name='item-list'),
    path('add-item/', add_item, name='item-add-list'),
    path('items/<int:pk>', get_one_item, name='get-one-item'),
    path('update_item/<int:pk>/', update_item, name='update_item'),

]
