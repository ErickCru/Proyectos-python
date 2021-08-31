from rest_framework import serializers
from ..models import Post


class PostModelSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'created', 'author', ]

    def get_author(self, obj):
        return obj.author.username

    def get_created(self, obj):
        return obj.created.strftime('%m-%d-%Y, %H:%M:%S')
