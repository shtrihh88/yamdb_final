from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import year_validator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name='category', max_length=256)
    slug = models.SlugField(
        verbose_name='category slug',
        unique=True,
        max_length=50
    )

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='genre', max_length=50)
    slug = models.SlugField(
        verbose_name='genre slug',
        unique=True,
        max_length=50
    )

    class Meta:
        ordering = ('slug',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(verbose_name='title', max_length=256)
    year = models.PositiveSmallIntegerField(
        verbose_name='year of issue',
        validators=[year_validator],
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='description',
        blank=True,
        null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='genre title'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='category title'
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Film',
    )
    text = models.TextField('Review text')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Author'
    )
    score = models.PositiveSmallIntegerField(
        'Rating',
        validators=[
            MinValueValidator(1, 'Valid values are from 1 to 10'),
            MaxValueValidator(10, 'Valid values are from 1 to 10')
        ]
    )
    pub_date = models.DateTimeField(
        'Pub date',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='one_review'
            )
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Review'
    )
    text = models.TextField('Comment text')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Author'
    )
    pub_date = models.DateTimeField(
        'Pub date', auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)
