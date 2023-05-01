from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Inicio"),
    path('login/', views.login, name="login"),
    path('campisite_category/', views.CampsiteListView, name="Lugares"  ),
]