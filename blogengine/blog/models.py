from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)
    body = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})
    