from django.db import models


class Recipe(models.Model):
    MAX_TITLE_LENGTH = 30

    MAX_INGREDIENTS_LENGTH = 250

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
    )

    image_url = models.URLField(
        verbose_name='Image URL'
    )

    description = models.TextField()

    ingredients = models.CharField(
        max_length=MAX_INGREDIENTS_LENGTH,
    )

    time = models.IntegerField(
        verbose_name='Time (Minutes)'
    )

    class Meta:
        ordering = ('id',)
