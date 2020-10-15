
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='IMDB MOVIE API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'swagger/', schema_view),
    path('api/', include('movies.urls'))
]
