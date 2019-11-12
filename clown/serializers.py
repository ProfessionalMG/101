from rest_framework import serializers

from .models import Appointment


class AppointmentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('client', 'clown', 'appointment_date', 'rating', 'status', 'issue')
