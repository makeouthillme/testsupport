from rest_framework_json_api import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('name', 'question', 'created_on', 'answer')
