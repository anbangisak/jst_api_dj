from django.urls import path
from random_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('random-list/', views.random_list),
    path('randoms/<int:pk>/', views.random_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
