# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from django.core.cache import cache
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from backend.users.serializers import UserSerializer, GroupSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib import auth


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

 
 
@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def login(request):
    receive = request.data
    username = receive.get('username')
    password = receive.get('password')
    user = auth.authenticate(username=username, password=password)
    if not user:
        msg = {"code": "-1", "msg": "用户名和密码不匹配"}
        return Response(msg, status=status.HTTP_401_UNAUTHORIZED)
    # 校验通过
    # 删除原有的Token
    old_token = Token.objects.filter(user=user)
    old_token.delete()
    # 创建新的Token
    token = Token.objects.create(user=user)

    msg = {"uid": user.id, "username": user.username, "api_token": token.key}
    return Response(msg)


@api_view(['POST'])
def logout(request):
    receive = request.data
    username = request.user
    user = User.objects.get(username=username)
    if not user:
        msg = {"data": {"code": "200", "msg": "退出"}}
        return Response(msg, status=status.HTTP_200_OK)

    old_token = Token.objects.filter(user=user)
    old_token.delete()
    msg = {"data": {"code": "200", "msg": "退出"}}
    return Response(msg, status=status.HTTP_200_OK)


@api_view(['POST'])
def do_something(request):
    receive = request.data
    print(receive)
    if request.user.is_authenticated:
        print("Do something...")
        return JsonResponse({"msg": "验证通过"})
    else:
        print("验证失败")
        return JsonResponse({"msg": "验证失败"})

