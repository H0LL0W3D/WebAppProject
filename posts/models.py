from django.conf import settings
from django.db import models
from django.urls import reverse
from crispy_forms.helper import FormHelper


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        blank="true",
        upload_to="screenshots",
        default="https://poster.keepcalmandposters.com/default/5773497_keep_calm_there_is_nothing_here.png",
    )

    # class Meta:
    #     ordering = ["date"].reverse

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
