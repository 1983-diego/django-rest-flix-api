from django.urls import path

from .views import ReviewCreateListView, ReviewRetriveUpdateDestroyView


urlpatterns = [
    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetriveUpdateDestroyView.as_view(), name='review-detail-view'),
]
