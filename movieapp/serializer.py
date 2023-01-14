from abc import ABC, ABCMeta

from rest_framework import serializers
from movieapp.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('name', 'movie_count',)

    def get_movies_count(self, director):
        return director.movie_count()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('title', 'description', 'duration', 'director', 'rating')

    def get_rating(self, movie):
        return movie.rating()

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

    def get_rating(self, movie):
        return movie.rating()

    def validate_name(self, name):
        name_exists = Director.objects.filter(name=name).exists()
        if not name_exists:
            return name
        raise ValidationError('Director already exists!')


class DirectorValidateSerializer(serializers.Serializer, metaclass=ABCMeta):
    name = serializers.CharField()

    def validate_director(self, director):
        if Director.objects.filter(id=director).count() == 0:
            raise ValidationError('Director with that id does not exists!')
        return director


    def validate_title(self, title):
        title_exists = Movie.objects.filter(title=title).exists()
        if not title_exists:
            return title
        raise ValidationError('Movies with this title already exists')


class MovieValidateSerializer(serializers.Serializer, metaclass=ABCMeta):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)
    director = serializers.IntegerField(required=True, min_value=1)



    def validate_movie(self, movie):
        movie_exists = Movie.objects.filter(id=movie).exists()
        if movie_exists:
            return movie
        raise ValidationError('Movie with this id does not exist')


class ReviewValidateSerializer(serializers.Serializer, ABC):
    text = serializers.CharField(required=True)
    stars = serializers.IntegerField(min_value=1, max_value=5, required=True)
    movie = serializers.IntegerField(min_value=1, required=True)






