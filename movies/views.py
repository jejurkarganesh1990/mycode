from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import MovieSerializer, GenreSerializer
from .models import Movie, Genre
from rest_framework.permissions import AllowAny, IsAdminUser

class MovieOperations(ModelViewSet):

    """
        retrive:
          return a movie instance.

        list:
            Return all movies, ordered by mostly joined.

        create:
            Create a new movie

        delete:
            Delete an existing movie.

        partial_update:
            Update one or more fields on an existing movie.

        update:
            Update a movie.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_permissions(self):
        if self.action == "list" :
            self.permission_classes = (AllowAny,)
        return super().get_permissions()

class GenreOperations(ModelViewSet):

    """
        retrive:
          return a Genre instance.

        list:
            Return all Genre, ordered by mostly joined.

        create:
            Create a new Genre.

        delete:
            Delete an existing Genre.

        partial_update:
            Update one or more fields on an existing Genre.

        update:
            Update a Genre.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = (AllowAny,)
        return super().get_permissions()