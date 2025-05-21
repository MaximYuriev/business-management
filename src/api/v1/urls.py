from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .users.views import CompanyViewSet, NewsViewSet

router = DefaultRouter()

router.register(r"companies", CompanyViewSet, basename="user_company")
router.register(r"news", NewsViewSet, basename="user_news")

urlpatterns = [
    path('users/', include(router.urls))
]
