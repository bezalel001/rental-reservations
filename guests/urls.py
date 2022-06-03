from django.urls import path 

from .views import HomePageView, RentalListView, RentalDetailView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('rentals/', RentalListView.as_view(), name='rental_list'),
  path('rentals/<uuid:pk>', RentalDetailView.as_view(), name='rental_detail' ),
]