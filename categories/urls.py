from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubcategoryViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"subcategories", SubcategoryViewSet, basename="subcategories")

urlpatterns = [
    path("", include(router.urls)),
]
