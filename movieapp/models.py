from django.db import models

class Name(models.Model):
    name = models.TextField()

class Coment(models.Model):
    text = models.TextField()

class Stars(models.Model):
    stars = models.DecimalField(max_digits=5, decimal_places=1)

class Movie(models.Model):
    title = models.ForeignKey(Name, on_delete=models.CASCADE)
    description = models.TextField()
    duration_min = models.PositiveIntegerField(null=True)
    director = models.CharField(max_length=250)

class Review(models.Model):
    text = models.ForeignKey(Coment, on_delete=models.CASCADE)
    movie = models.CharField(max_length=250)
    stars = models.ForeignKey(Stars, on_delete=models.CASCADE)


# Домашнее задание 2.
# Добавить к модели Review новое поле stars, в котором будет храниться значение
# от 1 до 5. stars поле в себе хранит рейтинг отзыва.
# Вывести на страницу список фильмов с их отзывами(reviews) -  /api/v1/movies/reviews/. а также
# вывести средний балл всех отзывов (rating)
# Вывести режиссеров /api/v1/directors/ с количеством фильмов (movies_count)

    # category = models.ForeignKey(Category, on_delete=models.CASCADE,
    #                              null=True)

    # post = models.ForeignKey(Post, on_delete=models.CASCADE,
    #                          related_name='comments')

