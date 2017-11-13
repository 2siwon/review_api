from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(
            username=username,
            password=password,
        )
        # 유저가 존재할 경우(authenticate 성공)
        if user:
            token, token_created = Token.objects.get_or_create(
                user=user,
            )
            data = {
                'token': token.key,
                'user': {
                    'pk': user.pk,
                    'username': user.username,
                    'img_profile': user.img_profile.url if user.img_profile else '',
                    'age': user.age,
                }
            }
            return Response(data, status=status.HTTP_200_OK)
        # 인증에 실패한 경우
        else:
            data = {
                'username': username,
                'password': password,
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
