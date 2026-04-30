# ChatGPT Acknowledgement
from django.urls import path

from . import views
from .views import PostCreate, PostDelete, PostList, PostUpdate

app_name = "discussionboard"

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("new/", PostCreate.as_view(), name="post_create"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("<slug:slug>/edit/", PostUpdate.as_view(), name="post_edit"),
    path("<slug:slug>/delete/", PostDelete.as_view(), name="post_delete"),
    path(
        "comment/<int:pk>/delete/", views.CommentDelete.as_view(), name="comment_delete"
    ),
    path("comment/<int:pk>/edit/", views.CommentUpdate.as_view(), name="comment_edit"),
]
