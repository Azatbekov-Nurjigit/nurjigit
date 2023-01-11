from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movieapp.serializer import *
from movieapp.models import Director, Movie, Review

@api_view(['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        directs = Director.objects.all()
        serializer = DirectorSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK,)
    elif request.method == 'POST':
        name = request.data.get('name')
        directs = Director.objects.create(name=name,)
        directs.save()
        return Response(data={'message': 'data received!', 'post': DirectorSerializer(directs).data})


@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        directs = Movie.objects.all()
        serializer = MovieSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        directs = Director.objects.create(title=title, description=description, duration=duration, director=director)
        directs.save()
        return Response(data={'message': 'data received!', 'post': MovieSerializer(directs).data})







@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        directs = Review.objects.all()
        serializer = ReviewSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        directs = Director.objects.create(text=text, stars=stars, movie=movie)
        directs.save()
        return Response(data={'message': 'data received!', 'post': ReviewSerializer(directs).data})












@api_view(['GET', 'DELETE', 'PUT'])
def director_detail_view(request, **kwargs):
    try:
        directs = Director.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Post not found!'})
    if request.method == 'GET':
        serializer = DirectorSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        directs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        directs.title = request.data.get('name')
        directs.save()
        return Response(data={'message': 'data received!', 'post': DirectorSerializer(directs).data})






@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail_view(request, **kwargs):
    try:
        directs = Movie.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Post not found!'})
    if request.method == 'GET':
        serializer = MovieSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        directs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        directs.title = request.data.get('title')
        directs.description = request.data.get('description')
        directs.duration = request.data.get('duration')
        directs.tags.set(request.data.get('tags'))
        directs.save()
        return Response(data={'message': 'data received!', 'post': MovieSerializer(directs).data})







@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_view(request, **kwargs):
    try:
        directs = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Post not found!'})
    if request.method == 'GET':
        serializer = ReviewSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        directs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        directs.text = request.data.get('text')
        directs.stars = request.data.get('stars')
        directs.save()
        return Response(data={'message': 'data received!', 'post': ReviewSerializer(directs).data})








@api_view(['GET'])
def rating(request):
    directs = Review.objects.all()
    serializer = ReviewSerializer(directs, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# Домашнее задание 3.
# Добавить создание режиссеров              /api/v1/directors/
# Добавить изменение и удаление режиссера   /api/v1/directors/<int:id>/
# Добавить создание фильмов                 /api/v1/movies/
# Добавить изменение и удаление фильм       /api/v1/movies/<int:id>/
# Добавить создание отзывов                 /api/v1/reviews/
# Добавить изменение и удаление отзыва      /api/v1/reviews/<int:id>/





