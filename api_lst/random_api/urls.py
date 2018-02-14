from django.urls import path
from random_api import views

urlpatterns = [
    path('random-list/', views.random_list),
    path('randoms/<int:pk>/', views.random_detail),
]