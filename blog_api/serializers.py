from rest_framework import serializers
from blog.models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')



class AuthorPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

class PostSerializer(serializers.ModelSerializer):
    author = AuthorPublicSerializer(read_only=True)
    title = serializers.CharField()

    class Meta: 
        model = Post
        fields = ('id', 'title', 'author')


    def create(self, validated_data):

        obj = super().create(validated_data)
        return obj