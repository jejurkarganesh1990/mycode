from rest_framework.serializers import ModelSerializer
from .models import Movie, Genre


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name',]


class MovieSerializer(ModelSerializer):
    genre = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


