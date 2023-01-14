from django.urls import path
from movieapp.views import director_list_view, movie_list_view, review_list_view, director_detail_view, movie_detail_view, \
    review_detail_view, rating


urlpatterns =[
    path('api/v1/directors/<int:id>/', director_detail_view),
    path('api/v1/movies/<int:id>/', movie_detail_view),
    path('api/v1/reviews/<int:id>/', review_detail_view),
    path('api/v1/directors/', director_list_view),
    path('api/v1/movies/', movie_list_view),
    path('api/v1/reviews/', review_list_view),
    path('api/v1/movies/reviews/', rating)
]




