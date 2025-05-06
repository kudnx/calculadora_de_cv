from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtefatoViewSet

router = DefaultRouter()
router.register(r'artefatos', ArtefatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]