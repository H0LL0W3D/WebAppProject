from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render

from .models import Post
from .forms import CommentForm
from django.db.models import Q


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post_list.html"


class SearchResultsView(ListView):
    model = Post
    template_name = "search_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query)
            | Q(body__icontains=query)
            | Q(comment__comment__icontains=query)
        )

        return object_list


# class PostDetailView(LoginRequiredMixin, DetailView):
#     model = Post
#     template_name = "post_detail.html"

#     def get_context_data(self, **kwargs):  # new
#         context = super().get_context_data(**kwargs)
#         context["form"] = CommentForm()
#         return context


class CommentGet(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    def post(self, reqeust, *args, **kwargs):
        self.object = self.get_object()
        return super().post(reqeust, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail", kwargs={"pk": post.pk})


class PostDetailView(LoginRequiredMixin, View):  # new
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = (
        "title",
        "body",
    )
    template_name = "post_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields = (
        "title",
        "body",
        "image",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Create your views here.
