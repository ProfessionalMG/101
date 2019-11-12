from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    fields = ['client', 'clown', 'appointment_date']

admin.site.register(Appointment, AppointmentAdmin)