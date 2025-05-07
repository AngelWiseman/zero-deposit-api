from django.urls import path
from .views import PropertyListCreateView, PropertyDetailView

urlpatterns = [
    path('', PropertyListCreateView.as_view(), name='property_list_create'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
]
