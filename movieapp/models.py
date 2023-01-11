from django.db import models
from django.contrib.auth.models import User

class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def movie_count(self):
        return self.movies.all().count()

class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    def rating(self):
        lists = [review.stars for review in self.reviews.all()]
        answer = sum(lists) / len(lists)
        return answer


STARS = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *')
)

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField()


    def __str__(self):
        return self.text

    def stars_str(self):
        return self.stars * '* '




# Домашнее задание 3.
# Добавить создание режиссеров              /api/v1/directors/
# Добавить изменение и удаление режиссера   /api/v1/directors/<int:id>/
# Добавить создание фильмов                 /api/v1/movies/
# Добавить изменение и удаление фильм       /api/v1/movies/<int:id>/
# Добавить создание отзывов                 /api/v1/reviews/
# Добавить изменение и удаление отзыва      /api/v1/reviews/<int:id>/
