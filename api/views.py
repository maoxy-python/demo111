from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    print("这是我的第一个视图")

    return HttpResponse("OK")


def user_login(request):
    """登录逻辑"""

    print("登录成功")

    return HttpResponse("Success")


def user_logout(request):
    print("登出")

    return HttpResponse("登出成功")


def test(request):
    return HttpResponse("OK")
