import random
import string

from django.db import models


def generate_random_string():
    characters = string.ascii_letters + string.digits
    return ''.join(x for x in random.choices(characters, k=8))


class Product(models.Model):
    title = models.TextField(max_length=1024)
    code = models.CharField(max_length=256, default=generate_random_string)
    article = models.CharField(max_length=256, blank=True)
    slug = models.SlugField(blank=True)
    status_code = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['updated_at']

    def __str__(self):
        return f'{self.title}'
