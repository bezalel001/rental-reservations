import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

class Rental(TimeStampedModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(_('name'), max_length=200, unique=True)  

  class Meta:
    ordering = ['name']

  def __str__(self):
    return '{} --- {}'.format(self.name, self.id)
  
  def get_absolute_url(self):
    return reverse('rental_detail', args=[str(self.id)])


class Reservation(TimeStampedModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  checkin = models.DateField(_('checkin'))
  checkout = models.DateField(_('checkout'))
  rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name='reservations', verbose_name=_('reservation'))  

  def clean(self):        
    if self.checkout < self.checkin:
        raise ValidationError({'checkout': _('Checkout cannot happen before checkin')})


  def __str__(self):
    return 'Res-{}'.format(self.id)
  


    


