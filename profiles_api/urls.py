from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, ProfileViewSet

router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello-viewset")
router.register("profile-viewset", ProfileViewSet)
urlpatterns = [
    path("hello-view/", HelloApiView.as_view(), name="hello_view"),
    path("", include(router.urls)),
]
