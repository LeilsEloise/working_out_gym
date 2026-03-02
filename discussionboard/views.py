# ChatGPT Code

from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Post


class PostList(generic.ListView):
    model = Post
    template_name = "discussionboard/post_list.html"
    context_object_name = "posts"
    ordering = ["-id"]  # safe even if you don't have created_on


@login_required
def post_vote(request, slug, value):
    post = get_object_or_404(Post, slug=slug)

    try:
        value = int(value)
    except ValueError:
        messages.error(request, "Invalid vote value.")
        return redirect("discussionboard:post_list")

    if value not in (-1, 1):
        messages.error(request, "Invalid vote.")
        return redirect("discussionboard:post_list")

    post.vote_total = (post.vote_total or 0) + value
    post.save(update_fields=["vote_total"])

    return redirect("discussionboard:post_list")