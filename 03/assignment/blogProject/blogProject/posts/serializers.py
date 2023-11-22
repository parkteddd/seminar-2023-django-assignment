from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = [
      "pk",
      "title",
      "content",
      "dt_created",
      "dt_modified",
      "author",
    ]
    read_only_fields = [
      "pk",
      "dt_created",
      "dt_modified",
      "author",
    ]
  