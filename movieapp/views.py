from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movieapp.serializer import *
from movieapp.models import Director, Movie, Review
from django.db import transaction



@api_view(['GET', 'POST'])
def director_list_view(request):
    if request.method == 'GET':
        directs = Director.objects.all()
        serializer = DirectorValidateSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK,)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data.get()
        directs = Director.objects.create(name=name,)
        directs.save()
        return Response(data={'message': 'data received!', 'post': DirectorValidateSerializer(directs).data})


@api_view(['GET', 'DELETE', 'PUT'])
def director_detail_view(request, **kwargs):
    try:
        directs = Director.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Post not found!'})
    if request.method == 'GET':
        serializer = DirectorValidateSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        directs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        directs.name = serializer.validated_data.get("name")
        directs.save()
        return Response(data={'message': 'data received!', 'post': DirectorValidateSerializer(directs).data})





@api_view(['GET', 'POST'])
def movie_list_view(request):
    if request.method == 'GET':
        directs = Movie.objects.all()
        serializer = MovieValidateSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description")
        duration = serializer.validated_data.get("duration")
        director = serializer.validated_data.get("director")
        directs = Director.objects.create(title=title, description=description, duration=duration, director=director)
        directs.save()
        return Response(data={'message': 'data received!', 'post': MovieValidateSerializer(directs).data})





@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail_view(request, **kwargs):
    try:
        directs = Movie.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Post not found!'})
    if request.method == 'GET':
        serializer = MovieValidateSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        directs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        directs.title = serializer.validated_data.get("title")
        directs.description = serializer.validated_data.get("description")
        directs.duration = serializer.validated_data.get("duration")
        directs.director_id = serializer.validated_data.get("director")
        directs.save()
        return Response(data={'message': 'data received!', 'post': MovieValidateSerializer(directs).data})






@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        directs = Review.objects.all()
        serializer = ReviewValidateSerializer(directs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get("text")
        stars = serializer.validated_data.get("stars")
        movie = serializer.validated_data.get("movie")
        with transaction.atomic():
            reviews = Review.objects.create(text=text, stars=stars, movie_id=movie)
            reviews.save()
            return Response(data={"massage": "Review created successfully!",
                                  "reviews": ReviewValidateSerializer(reviews).data},
                            status=status.HTTP_201_CREATED)















@api_view(['GET', 'DELETE', 'PUT'])
def review_detail_view(request, **kwargs):
    try:
        directs = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Post not found!'})
    if request.method == 'GET':
        serializer = ReviewValidateSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        directs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        directs.text = serializer.validated_data.get("text")
        directs.stars = serializer.validated_data.get("stars")
        directs.movie_id = serializer.validated_data.get("movie")
        directs.save()
        return Response(data={'message': 'data received!', 'post': ReviewValidateSerializer(directs).data})








@api_view(['GET'])
def rating(request):
    directs = Review.objects.all()
    serializer = ReviewSerializer(directs, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# Домашнее задание 4.
# Написать валидацию на все API
# /api/v1/directors/
# /api/v1/directors/<int:id>/
# /api/v1/movies/
# /api/v1/movies/<int:id>/
# /api/v1/reviews/
# /api/v1/reviews/<int:id>/








