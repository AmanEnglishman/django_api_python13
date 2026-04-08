from django.urls import path

from .views import FirstAPI

urlpatterns = [
    path('api/', FirstAPI.as_view()),
]
