from django.urls import path
from .views import enter_million_rows

urlpatterns = [
    path('million-rows/',enter_million_rows,name='enter-million-rows')
]