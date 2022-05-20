from rest_framework import generics, permissions
from .serializers import LikesSerializer
from .models import Likes
from .permissions import IsAuthor

class LikesView(generics.ListAPIView):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()


class LikesCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikesDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthor,)
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer



