from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/authorization/', views.authorization),
    path('api/v1/users/registration/', views.registration),
]

