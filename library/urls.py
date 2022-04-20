from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.home),
    path('new_book/<int:pk>/', views.update),
    path('getc/', views.get_category),
]
