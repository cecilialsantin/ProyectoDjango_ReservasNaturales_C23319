from django.urls import include, path
from rest_framework import routers
from .views import ReservationViewSet

router = routers.DefaultRouter()
router.register('reservationsrest', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]