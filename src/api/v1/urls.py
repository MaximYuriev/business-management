from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .users.views import CompanyViewSet, NewsViewSet, UserViewSet

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="user")
router.register(r"companies", CompanyViewSet, basename="user_company")
router.register(r"news", NewsViewSet, basename="user_news")

urlpatterns = [
    path('v1/', include(router.urls))
]
