from django.views.generic import TemplateView, ListView, DetailView

from .models import Rental


class HomePageView(TemplateView):
  template_name = 'home.html'


class RentalListView(ListView):
  model = Rental 
  context_object_name = 'rental_list'
  template_name = 'guests/rental_list.html'

class RentalDetailView(DetailView):
  model = Rental
  template_name = 'guests/rental_detail.html'
