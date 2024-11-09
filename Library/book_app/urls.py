from django.urls import path
from .views import world_books, ukr_books

urlpatterns = [
    path('ukr_lit/', ukr_books, name = "ukr_lit"),
    path('world_lit/', world_books, name = "world_lit")
]