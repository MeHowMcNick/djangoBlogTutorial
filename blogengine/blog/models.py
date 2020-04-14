from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    slug = slugify(s, allow_unicode=True)
    return slug + f'-{int(time())}'


class Post(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    body = models.TextField(blank=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})
    