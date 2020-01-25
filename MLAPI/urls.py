from django.urls import path
from .views import *
urlpatterns = [
    path('she_mad/',she_mad_model.as_view(), name="she_mad" ),
]
