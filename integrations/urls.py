from django.urls import path

from .views import WeatherView, CurrencyView, HolidayView

urlpatterns = [
    path('weather/', WeatherView.as_view()),
    path('currency/', CurrencyView.as_view()),
    path('holiday/', HolidayView.as_view()),
]