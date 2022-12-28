from rest_framework import serializers
from movieapp.models import *

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('name',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('title','description','duration_min','director')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('text', 'movie')


