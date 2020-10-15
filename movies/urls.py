from rest_framework.routers import SimpleRouter
from .views import MovieOperations, GenreOperations

router = SimpleRouter()
router.register('movie',MovieOperations)
router.register('genre',GenreOperations)
urlpatterns= router.urls