#ChatGPT code

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.text import slugify

from .models import Post

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


class PostDetail(generic.DetailView):
    model = Post
    template_name = "discussionboard/post_detail.html"
    context_object_name = "post"

class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]  # add fields you actually have
    template_name = "discussionboard/post_form.html"
    success_url = reverse_lazy("discussionboard:post_list")

    def form_valid(self, form):
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

    def get_success_url(self):
        return reverse_lazy("discussionboard:post_detail", kwargs={"slug": self.object.slug})

class PostDelete(LoginRequiredMixin, PostOwnerOrSuperuserMixin, generic.DeleteView):
    model = Post
    template_name = "discussionboard/post_confirm_delete.html"
    success_url = reverse_lazy("discussionboard:post_list")


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