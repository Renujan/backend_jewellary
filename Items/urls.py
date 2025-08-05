from django.urls import path
from Items.views import ItemsListView, ItemDetailView

urlpatterns = [
    path('api/items/', ItemsListView.as_view(), name='items-list'),
    path('api/items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]