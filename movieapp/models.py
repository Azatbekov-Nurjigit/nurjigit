from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=250)

class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    duration_min = models.PositiveIntegerField(null=True)
    director = models.CharField(max_length=250)
class Review(models.Model):
    text = models.TextField()
    movie = models.CharField(max_length=250)








# Вывести список режиссеров /api/v1/directors/
# Вывести одного режиссера   /api/v1/directors/<int:id>/
#
# Вывести список фильмов      /api/v1/movies/
# Вывести один фильм             /api/v1/movies/<int:id>/
#
# Вывести список отзывов       /api/v1/reviews/
# Вывести один отзыв              /api/v1/reviews/<int:id>/

