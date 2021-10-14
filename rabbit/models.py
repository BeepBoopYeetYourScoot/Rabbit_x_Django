from django.db import models


class Product(models.Model):
    title = models.TextField(max_length=1024)
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
