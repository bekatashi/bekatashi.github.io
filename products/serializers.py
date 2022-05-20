from rest_framework import serializers

from . models import Product, Comment, Favorites


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('author', )


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'owner', 'product', 'created_at')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        exclude = ('user',)

