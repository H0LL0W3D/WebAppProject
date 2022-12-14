from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    SearchResultsView,
)

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("search/", SearchResultsView.as_view(), name="search_list"),
    path("", PostListView.as_view(), name="post_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
