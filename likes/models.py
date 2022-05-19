from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Likes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'

    def __str__(self): return f'{self.product} liked'

