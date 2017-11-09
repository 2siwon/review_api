# PostList를 리턴하는 APIView를 만드세요
# 근데 APIView를 상속받도록
# get요청만 응답
from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer


class PostList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


        # PostDetail APIView 생성
        # APIView를 사용
        # class PostDetail(APIView):
        # def get(self, request, pk):
        #     post = Post.objects.get(pk=pk)
        #     serializer = PostSerializer(post)
        #     return Response(serializer.data)
