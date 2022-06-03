from django.contrib import admin
from .models import Rental, Reservation 


class ReservationInline(admin.TabularInline):
  model = Reservation



class RentalAdmin(admin.ModelAdmin):
  inlines = [ReservationInline,]
  list_display = ('name', )



admin.site.register(Rental, RentalAdmin)
