from django.urls import path

from . import views  # import your views here

urlpatterns = [
    path('', views.home, name='home'),  # example URL pattern
    path('todos/', views.todos, name='Todos'),  # another example URL pattern
]
