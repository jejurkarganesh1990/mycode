from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import MovieSerializer, GenreSerializer
from .models import Movie, Genre
from rest_framework.permissions import AllowAny, IsAdminUser

class MovieOperations(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_permissions(self):
        if self.action == "list" :
            self.permission_classes = (AllowAny,)
        return super().get_permissions()

class GenreOperations(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = (AllowAny,)
        return super().get_permissions()