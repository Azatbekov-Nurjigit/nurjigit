from rest_framework import serializers
from movieapp.models import *

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'director',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','description','duration_min','director')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'movie', 'stars')



        # Домашнее задание 2.
# Добавить к модели Review новое поле stars, в котором будет храниться значение
# от 1 до 5. stars поле в себе хранит рейтинг отзыва.
# Вывести на страницу список фильмов с их отзывами(reviews) -  /api/v1/movies/reviews/. а также
# вывести средний балл всех отзывов (rating)
# Вывести режиссеров /api/v1/directors/ с количеством фильмов (movies_count)

