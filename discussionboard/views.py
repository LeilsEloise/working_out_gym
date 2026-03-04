#ChatGPT code

from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CommentForm
from .models import Post, Comment

class PostList(generic.ListView):
    model = Post
    template_name = "discussionboard/post_list.html"
    context_object_name = "posts"
    paginate_by = 10
    ordering = ["-created_on"]  # if you have created_on, otherwise use ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context["my_posts"] = Post.objects.filter(
                author=self.request.user
            ).order_by("-created_on")
        else:
            context["my_posts"] = Post.objects.none()

        return context

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # get comments for this post (adjust names to your model)
    comments = post.comments.all().order_by("-created_on")  # or "-id"

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("account_login")

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.Post = post
            comment.author = request.user  # adjust field name if yours is "user" etc
            comment.save()
            messages.success(request, "Your comment has been posted.")
            return redirect("discussionboard:post_detail", slug=post.slug)
        else:
            messages.error(request, "Couldn’t post comment — please check the form.")

    else:
        comment_form = CommentForm()

    return render(
        request,
        "discussionboard/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        },
    )    


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]  # add fields you actually have
    template_name = "discussionboard/post_form.html"
    success_url = reverse_lazy("discussionboard:post_list")

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        form.instance.author = self.request.user
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

class PostOwnerOrSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        post = self.get_object()
        return self.request.user.is_superuser or post.author == self.request.user

class PostUpdate(LoginRequiredMixin, PostOwnerOrSuperuserMixin, generic.UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "discussionboard/post_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("discussionboard:post_detail", kwargs={"slug": self.object.slug})

class PostDelete(LoginRequiredMixin, PostOwnerOrSuperuserMixin, generic.DeleteView):
    model = Post
    template_name = "discussionboard/post_confirm_delete.html"
    success_url = reverse_lazy("discussionboard:post_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted.")
        return super().delete(request, *args, **kwargs)

#ChatGPT Code
class CommentOwnerOrSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        comment = self.get_object()
        return self.request.user.is_superuser or comment.author == self.request.user

#ChatGPT Code
class CommentDelete(LoginRequiredMixin, CommentOwnerOrSuperuserMixin, generic.DeleteView):
    model = Comment
    template_name = "discussionboard/comment_confirm_delete.html"

    def get_success_url(self):
        # send user back to the post detail page after deleting the comment
        return reverse_lazy("discussionboard:post_detail", kwargs={"slug": self.object.Post.slug})

#ChatGPT Code
class CommentOwnerOrSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        comment = self.get_object()
        return self.request.user.is_superuser or comment.author == self.request.user

#ChatGPT Code
class CommentUpdate(LoginRequiredMixin, CommentOwnerOrSuperuserMixin, generic.UpdateView):
    model = Comment
    fields = ["body"]
    template_name = "discussionboard/comment_form.html"

    def get_success_url(self):
        return reverse_lazy("discussionboard:post_detail", kwargs={"slug": self.object.Post.slug})

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