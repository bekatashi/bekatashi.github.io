from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    def __str__(self): return f'{self.title} (Price: {self.price})'


class Comment(models.Model):
    body = models.TextField()
    product = models.ForeignKey(Product, related_name='comment', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ('created_at',)

    def __str__(self): return f'{self.owner} - {self.body}'


class Favorites(models.Model):
    product = models.ForeignKey(Product, related_name='favorite', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='favorite', on_delete=models.CASCADE)
