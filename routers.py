from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from library.views.publishers import PublisherViewSet


router = SimpleRouter()
# router = DefaultRouter()
router.register('publisher', PublisherViewSet)  # /api/v1/publishers/
                                                      # /api/v1/publishers/<pk>


urlpatterns = [
    path('books/', include('library.urls.books')),
    path('users/', include('library.urls.users')),
    path('categories/', include('library.urls.categories')),
] + router.urls
