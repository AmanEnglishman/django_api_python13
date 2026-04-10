from django.urls import path

from .views import TodoListAPI, TodoCreateAPI, TodoUpdateAPI, TodoDeleteAPI

urlpatterns = [
    path('list/', TodoListAPI.as_view()),
    path('create/', TodoCreateAPI.as_view()),
    path('<int:pk>/update/', TodoUpdateAPI.as_view()),
    path('<int:pk>/delete/', TodoDeleteAPI.as_view())
]