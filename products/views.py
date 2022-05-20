from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . models import Product, Comment, Favorites
from products.serializers import ProductSerializer
from . permissions import IsAuthor, IsSuperUser
from rest_framework import views
from rest_framework.viewsets import ModelViewSet


class PaginationClass(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 1000


class ProductCreateView(generics.CreateAPIView):
    permission_classes = (IsSuperUser,)
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationClass
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('author', 'price')
    search_fields = ('title',)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthor,)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAuthor)


class FavoritesViewset(ModelViewSet):
    class Meta:
        fields = '__all__'
        model = Favorites
    queryset = Favorites.objects.all()
    serializer_class = serializers.FavoritesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

