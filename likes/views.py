from rest_framework import generics, permissions
from .serializers import LikesSerializer
from .models import Likes


class LikesView(generics.ListAPIView):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()


class LikesCreateView(generics.CreateAPIView):
    permission_classes = permissions.AllowAny
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

