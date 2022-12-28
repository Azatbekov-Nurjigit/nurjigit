from django.urls import path
from movieapp.views import *

urlpatterns =[
    path('api/v2/directors/<int:id>/', directorr),
    path('api/v2/movies/<int:id>/', moviee),
    path('api/v2/reviews/<int:id>/', Revieww),
    path('api/v2/directors/', directorrr),
    path('api/v2/movies/', movieee),
    path('api/v2/reviews/', Reviewww),
]


# Вывести список режиссеров /api/v1/directors/
# Вывести одного режиссера   /api/v1/directors/<int:id>/

# Вывести список фильмов      /api/v1/movies/
# Вывести один фильм             /api/v1/movies/<int:id>/

# Вывести список отзывов       /api/v1/reviews/
# Вывести один отзыв              /api/v1/reviews/<int:id>/





