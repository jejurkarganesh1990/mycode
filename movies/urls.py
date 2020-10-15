from rest_framework.routers import SimpleRouter
from .views import MovieOperations, GenreOperations

router = SimpleRouter()
router.register('imdb/movie',MovieOperations)
router.register('imdb/genre',GenreOperations)
urlpatterns= router.urls