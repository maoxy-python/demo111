from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    print("这是我的第一个视图")

    return HttpResponse("OK")
