#ChatGPT Acknowledgement
from django.urls import path
from . import views

app_name = "discussionboard"

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("vote/<slug:slug>/<int:value>/", views.post_vote, name="post_vote"),
]