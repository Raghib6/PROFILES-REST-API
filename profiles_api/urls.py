from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    HelloApiView,
    HelloViewSet,
    ProfileViewSet,
    UserLoginView,
    UserProfileFeedViewSet,
)

router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, basename="hello-viewset")
router.register("profile-viewset", ProfileViewSet)
router.register("feed", UserProfileFeedViewSet)
urlpatterns = [
    path("hello-view/", HelloApiView.as_view(), name="hello_view"),
    path("login/", UserLoginView.as_view()),
    path("", include(router.urls)),
]
