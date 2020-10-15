from rest_framework.routers import SimpleRouter
from .views import MovieOperations, GenreOperations

router = SimpleRouter()
router.register('api/movie',MovieOperations)
router.register('api/genre',GenreOperations)
urlpatterns= router.urls