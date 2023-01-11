from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movieapp.serializer import *
from movieapp.models import *


@api_view(['GET'])
def directorrr(request):
    if request.method == 'GET':
        directs = Movie.objects.all()
        serializer = DirectorSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def movieee(request):
    if request.method == 'GET':
        directs = Movie.objects.all()
        serializer = MovieSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Reviewww(request):
    if request.method == 'GET':
        directs = Review.objects.all()
        serializer = ReviewSerializer(directs, many=True)
        print(serializer)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




# @api_view(['GET'])
# def directorr(request, **kwargs):
#     if request.method == 'GET':
#         try:
#             directs = Director.objects.get(id=kwargs['id'])
#         except Director.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data={'message': 'Post not found!'})
#         serializer = DirectorSerializer(directs, many=False)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
# @api_view(['GET'])
# def moviee(request, **kwargs):
#     if request.method == 'GET':
#         try:
#             directs = Movie.objects.get(id=kwargs['id'])
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data={'message': 'Post not found!'})
#         serializer = MovieSerializer(directs, many=False)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
# @api_view(['GET'])
# def Revieww(request, **kwargs):
#     if request.method == 'GET':
#         try:
#             directs = Review.objects.get(id=kwargs['id'])
#         except Review.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data={'message': 'Post not found!'})
#         serializer = ReviewSerializer(directs, many=False)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)







# @api_view(['GET'])
# def rating(request):
#     if request.method == 'GET':
#         directs = Movie.objects.all()
#         serializer = RatingSerializer(directs, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


# Домашнее задание 2.
# Добавить к модели Review новое поле stars, в котором будет храниться значение
# от 1 до 5. stars поле в себе хранит рейтинг отзыва.
# Вывести на страницу список фильмов с их отзывами(reviews) -  /api/v1/movies/reviews/. а также
# вывести средний балл всех отзывов (rating)
# Вывести режиссеров /api/v1/directors/ с количеством фильмов (movies_count)
