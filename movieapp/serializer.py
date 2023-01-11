from rest_framework import serializers
from movieapp.models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('name', 'movie_count',)

    def get_director_count(self, director):
        return director.movie_count()


class MovieSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ('title', 'description', 'duration', 'director', 'stars_count')

    def get_rating(self, rat):
        return rat.rating

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'movie', 'stars',)

class RatingSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    review = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id rating title description duration director reviews movie'.split()

    def getrating(self, rat):
        return rat.rating

    # Домашнее задание 3.
    # Добавить создание режиссеров              /api/v1/directors/
    # Добавить изменение и удаление режиссера   /api/v1/directors/<int:id>/
    # Добавить создание фильмов                 /api/v1/movies/
    # Добавить изменение и удаление фильм       /api/v1/movies/<int:id>/
    # Добавить создание отзывов                 /api/v1/reviews/
    # Добавить изменение и удаление отзыва      /api/v1/reviews/<int:id>/

