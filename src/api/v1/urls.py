from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .users.views import CompanyViewSet, NewsViewSet, UserViewSet, TaskViewSet

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="user")
router.register(r"companies", CompanyViewSet, basename="company")
router.register(r"news", NewsViewSet, basename="news")
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path('v1/', include(router.urls)),
    path("v1/auth/", include("rest_framework.urls")),
]
