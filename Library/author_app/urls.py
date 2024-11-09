from django.urls import path
from .views import show_ukr_au, show_world_au

urlpatterns = [
    path('ukr_au/', show_ukr_au, name = "ukr_au"),
    path('world_au/', show_world_au, name = "world_au")
]
