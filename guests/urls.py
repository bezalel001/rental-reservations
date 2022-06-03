from django.urls import path 

from .views import HomePageView, RentalListView, RentalDetailView, ReservationListView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('rentals/', RentalListView.as_view(), name='rental_list'),
  path('rentals/<uuid:pk>', RentalDetailView.as_view(), name='rental_detail' ),
  path('reservations/', ReservationListView.as_view(), name='reservations_table' ),
]