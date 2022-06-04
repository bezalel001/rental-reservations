from datetime import datetime
from django.test import SimpleTestCase, Client, TestCase
from django.urls import reverse, resolve

from .views import HomePageView
from .models import Rental, Reservation

class HomepageTests(SimpleTestCase):

  def setUp(self):
    url = reverse('home')
    self.response = self.client.get(url)

  def test_homepage_status_code(self):
    self.assertEqual(self.response.status_code, 200)
  
  def test_homepage_template(self):
    self.assertTemplateUsed(self.response, 'home.html')

  def test_homepage_contains_correct_html(self):
    self.assertContains(self.response, 'Welcome To Rentals and Reservations')

  def test_homepage_does_not_contain_incorrect_html(self):
    self.assertNotContains(self.response, 'Hello! I should not be here')
  
  def test_hompage_url_resolves_hompageview(self):
    view = resolve('/')
    self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class RentalTests(TestCase):
  def setUp(self):
    self.rental = Rental.objects.create(name='rental-1')
    self.reservation = Reservation.objects.create(rental=self.rental, checkin=datetime(year=2016, month=5, day=23), checkout=datetime(year=2016, month=5, day=6))

  
  def test_rental_listing(self):
    self.assertEqual(f'{self.rental.name}', 'rental-1')
  
  def test_rental_list_view(self):
    response = self.client.get(reverse('rental_list'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'rental-1')
    self.assertTemplateUsed(response, 'guests/rental_list.html')
  
  def test_rental_detail_view(self):
    response = self.client.get(self.rental.get_absolute_url())
    no_response = self.client.get('/rentals/12345/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(no_response.status_code, 404)
    self.assertContains(response, 'rental-1')
    self.assertContains(response, 'May 23, 2016')
    self.assertTemplateUsed(response, 'guests/rental_detail.html')



class ReservationTests(TestCase):
  def setUp(self):
    self.rental1 = Rental.objects.create(name='rental-1')
    Reservation.objects.create(rental=self.rental1, checkin=datetime(year=2016, month=5, day=23), checkout=datetime(year=2017, month=5, day=6))
    Reservation.objects.create(rental=self.rental1, checkin=datetime(year=2017, month=7, day=23), checkout=datetime(year=2018, month=5, day=6))


    self.rental2 = Rental.objects.create(name='rental-2')
    Reservation.objects.create(rental=self.rental2, checkin=datetime(year=2020, month=5, day=5), checkout=datetime(year=2020, month=6, day=6))
    Reservation.objects.create(rental=self.rental2, checkin=datetime(year=2021, month=3, day=2), checkout=datetime(year=2021, month=4, day=17))

    self.response = self.client.get(reverse('reservations_table'))
 
  
  def test_reservation_list_view(self):    
    self.assertEqual(self.response.status_code, 200)
    self.assertContains(self.response, 'Reservations Table')
    self.assertContains(self.response, 'Rental Name')
    self.assertContains(self.response, 'Reservation ID')
    self.assertContains(self.response, 'Checkin')
    self.assertContains(self.response, 'Checkout')
    self.assertContains(self.response, 'Previous Reservation ID')
    self.assertTemplateUsed(self.response, 'guests/reservations.html')
  
  def test_reservation_list_view_incorrect(self): 
    no_response = self.client.get('/reservations/12345/')    
    self.assertEqual(no_response.status_code, 404)
  
  def test_reservation_table_rentals(self):    
    self.assertEqual(self.response.status_code, 200)
    self.assertContains(self.response, 'rental-1')
    self.assertContains(self.response, 'rental-2')

  def test_reservation_table_reservations_checkins(self):
    self.assertEqual(self.response.status_code, 200)
    self.assertContains(self.response, 'May 23, 2016')
    self.assertContains(self.response, 'July 23, 2017')
    self.assertContains(self.response, 'May 5, 2020')
    self.assertContains(self.response, 'March 2, 2021')

  def test_reservation_table_reservations_checkouts(self):    
    self.assertEqual(self.response.status_code, 200)   
    self.assertContains(self.response, 'May 6, 2017')
    self.assertContains(self.response, 'May 6, 2018')
    self.assertContains(self.response, 'June 6, 2020')
    self.assertContains(self.response, 'April 17, 2021')
    
   


