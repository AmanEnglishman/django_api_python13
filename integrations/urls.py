from django.urls import path

from .views import WeatherView, CurrencyView

urlpatterns = [
    path('weather/', WeatherView.as_view()),
    path('currency/', CurrencyView.as_view()),
]