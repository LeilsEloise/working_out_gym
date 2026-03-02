# ChatGPT Code

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views import generic

from .models import Post

#ChatGPT Code 
class PostList(generic.ListView):
    model = Post
    template_name = "discussionboard/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_on"]  # if you have created_on

@login_required
def post_vote(request, slug, value):
    post = get_object_or_404(Post, slug=slug)

    if value not in (-1, 1):
        messages.error(request, "Invalid vote.")
        return redirect("discussionboard:post_list")

    # Simple approach: store total on Post (you need vote_total IntegerField on Post)
    post.vote_total = (post.vote_total or 0) + value
    post.save(update_fields=["vote_total"])

    return redirect("discussionboard:post_list")