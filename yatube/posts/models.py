from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='name'
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        verbose_name='address'
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='description of group'
    )

    def __str__(self):
        return self.title


class Post(models.Model):

    text = models.TextField(
        verbose_name='content'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='publish date'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author of post'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='posts',
        verbose_name='group'
    )

    class Meta:
        ordering = ['-pub_date']
