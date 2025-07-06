from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.ListingListCreate.as_view(), name='listing-list-create'),
    path('listings/<int:pk>/', views.ListingDetail.as_view(), name='listing-detail'),
]