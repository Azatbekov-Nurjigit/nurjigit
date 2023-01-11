from django.urls import path
from movieapp.views import *

urlpatterns =[
    # path('api/v1/directors/<int:id>/', directorr),
    # path('api/v1/movies/<int:id>/', moviee),
    # path('api/v1/reviews/<int:id>/', Revieww),
    path('api/v1/directors/', directorrr),
    path('api/v1/movies/', movieee),
    path('api/v1/reviews/', Reviewww),
    # path('/api/v1/movies/reviews/', rating),
]

# Домашнее задание 2.
# Добавить к модели Review новое поле stars, в котором будет храниться значение
# от 1 до 5. stars поле в себе хранит рейтинг отзыва.
# Вывести на страницу список фильмов с их отзывами(reviews) -  /api/v1/movies/reviews/. а также
# вывести средний балл всех отзывов (rating)
# Вывести режиссеров /api/v1/directors/ с количеством фильмов (movies_count)





