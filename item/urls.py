from django.urls import path
from .views import item_list

urlpatterns = [
    path('items/', item_list, name='item-list'),
    # path('add-item/', add_item, name='item-add-list'),
]
