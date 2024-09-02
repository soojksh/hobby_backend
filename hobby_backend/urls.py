
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
import places.views
import songs.views
import movies.views
import books.views
from django.conf import settings
from django.conf.urls.static import static



router = routers.DefaultRouter()
router.register(r'books', books.views.BookView, 'book')
router.register(r'places', places.views.PlaceViewSet, 'place')
router.register(r'songs', songs.views.SongViewSet, 'song')
router.register(r'movies', movies.views.MovieViewSet, 'movie')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
