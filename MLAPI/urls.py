from django.urls import path, include
from .views import *
urlpatterns = [
    path('she_mad/',she_mad_model.as_view(), name="she_mad" ),
]
