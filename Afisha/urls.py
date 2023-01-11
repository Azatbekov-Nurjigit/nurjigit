"""Afisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from movieapp.views import *
urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('movieapp.urls') ),
]



# Домашнее задание 2.
# Добавить к модели Review новое поле stars, в котором будет храниться значение
# от 1 до 5. stars поле в себе хранит рейтинг отзыва.
# Вывести на страницу список фильмов с их отзывами(reviews) -  /api/v1/movies/reviews/. а также
# вывести средний балл всех отзывов (rating)
# Вывести режиссеров /api/v1/directors/ с количеством фильмов (movies_count)





