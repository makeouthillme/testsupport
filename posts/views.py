from rest_framework import viewsets
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


class PostViewset(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    model = Post
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        postssup = Post.objects.all()
        return self.model.objects.all()