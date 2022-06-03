import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Rental(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(_('name'), max_length=200, unique=True)

  def __str__(self):
    return '{}-{}'.format(self.name, self.id)

  
  def get_absolute_url(self):
    return reverse('rental_detail', args=[str(self.id)])



class Reservation(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  checkin = models.DateField(_('checkin'))
  checkout = models.DateField(_('checkout'))
  rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name='reservations', verbose_name=_('reservation'),)

  def __str__(self):
    return 'Res-{}'.format(self.id)


