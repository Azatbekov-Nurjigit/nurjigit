from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movieapp.models import *
from movieapp.serializer import *

@api_view(['GET'])
def directorrr(request):
    if request.method == 'GET':
        directs = Director.objects.all()
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
        return Response(data=serializer.data, status=status.HTTP_200_OK)




@api_view(['GET'])
def directorr(request, **kwargs):
    if request.method == 'GET':
        try:
            directs = Director.objects.get(id=kwargs['id'])
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Post not found!'})
        serializer = DirectorSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)








@api_view(['GET'])
def moviee(request, **kwargs):
    if request.method == 'GET':
        try:
            directs = Movie.objects.get(id=kwargs['id'])
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Post not found!'})
        serializer = MovieSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)







@api_view(['GET'])
def Revieww(request, **kwargs):
    if request.method == 'GET':
        try:
            directs = Review.objects.get(id=kwargs['id'])
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'Post not found!'})
        serializer = ReviewSerializer(directs, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)






# Вывести список режиссеров /api/v1/directors/
# Вывести одного режиссера   /api/v1/directors/<int:id>/
#
# Вывести список фильмов      /api/v1/movies/
# Вывести один фильм             /api/v1/movies/<int:id>/
#
# Вывести список отзывов       /api/v1/reviews/
# Вывести один отзыв              /api/v1/reviews/<int:id>/



# from rest_framework import status
#
# @api_view(['GET'])
# def posts_view(request):
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET'])
# def post_detail_view(request, **kwargs):
#     if request.method == 'GET':
#         try:
#             post = Post.objects.get(id=kwargs['id'])
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND,
#                             data={'message': 'Post not found!'})
#         serializer = PostSerializer(post, many=False)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
