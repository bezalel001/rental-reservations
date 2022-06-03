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
    self.assertContains(self.response, 'Table of Reservations<')

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

