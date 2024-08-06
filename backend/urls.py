from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import albumsDataViewSet
from .views import songsDataViewSet

router = DefaultRouter()
router.register(r'albums', albumsDataViewSet)
router.register(r'songs', songsDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]