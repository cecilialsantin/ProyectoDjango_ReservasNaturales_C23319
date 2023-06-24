from rest_framework import serializers
from administracion.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = '__all__'
    
