from django.urls import path

from .views import ArticleViewSet, TagViewSet

urlpatterns = [
    path(
        "articles",
        ArticleViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "articles/<str:pk>",
        ArticleViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
path(
        "tags",
        TagViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "tags/<str:pk>",
        TagViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]