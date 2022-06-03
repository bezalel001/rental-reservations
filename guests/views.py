from django.views.generic import TemplateView, ListView, DetailView

from .models import Rental, Reservation


class HomePageView(TemplateView):
  template_name = 'home.html'


class RentalListView(ListView):
  model = Rental 
  context_object_name = 'rental_list'
  template_name = 'guests/rental_list.html'  

class RentalDetailView(DetailView):
  model = Rental
  template_name = 'guests/rental_detail.html'

  def get_context_data(self, **kwargs):
    context = super(RentalDetailView, self).get_context_data(**kwargs)
    reservations = Reservation.objects.filter(rental=self.object).order_by('-created')[:1]
    context['reservations'] = reservations
    return context

class ReservationListView(ListView):
  model = Reservation
  context_object_name = 'reservations'
  template_name = 'guests/reservations.html'


  def get_queryset(self):
    queryset = Reservation.objects.all().order_by('rental__name', 'created')
    return queryset

    # data = {}
    # size = len(queryset)

    # for i in range(1, size):
      
    #   if queryset[i].rental.id == queryset[i-1].rental.id:
    #      data[queryset[i].rental] = 






  # def get_context_data(self, **kwargs):
  #   context = super(ReservationListView, self).get_context_data(**kwargs)
  #   size = len(self.queryset)
  #   previous ={}
  #   for i in range(1, size):
  #     if self.queryset[i].rental.id == self.queryset[i-1].rental.id:
  #       previous[self.queryset[i].rental.name] = self.queryset[i-1].id
  #   context['previous_reservations'] = previous
  #   return context




