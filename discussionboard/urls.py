#ChatGPT Acknowledgement
from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete

app_name = "discussionboard"

urlpatterns = [
 path("", PostList.as_view(), name="post_list"),
    path("new/", PostCreate.as_view(), name="post_create"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("<slug:slug>/edit/", PostUpdate.as_view(), name="post_edit"),
    path("<slug:slug>/delete/", PostDelete.as_view(), name="post_delete"),
]