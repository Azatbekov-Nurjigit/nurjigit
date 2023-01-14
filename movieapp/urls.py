from django.urls import path
from .views import *
# from movieapp.views import director_list_view, movie_list_view, review_list_view, director_detail_view, movie_detail_view, \
#     review_detail_view, rating
LIST_CREATE = {'get': 'list', 'post': 'create'}
RETRIEVE_UPDATE_DESTROY = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}


urlpatterns =[
    path('directors/', DirectorModelViewSet.as_view(LIST_CREATE)),
    path('directors/<int:id>/', DirectorModelViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
    path('movies/', MovieModelViewSet.as_view(LIST_CREATE)),
    path('movies/<int:id>/', MovieModelViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
    path('reviews/', ReviewModelViewSet.as_view(LIST_CREATE)),
    path('reviews/<int:id>/', ReviewModelViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
]




