from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from rest_framework import viewsets

from .models import Appointment
from .serializers import AppointmentSerializers


# Create your views here.
class AppointmentView(LoginRequiredMixin, ListView):
    login_url = 'restframework/login'
    model = Appointment
    context_object_name = 'bookings'

    def get_context_data(self, **kwargs):
        context = super(AppointmentView, self).get_context_data(**kwargs)
        return context


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    login_url = 'restframework/login'
    model = Appointment


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
