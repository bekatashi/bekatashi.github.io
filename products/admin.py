from django.contrib import admin

from products.models import Product, Comment, Favorites

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Favorites)
