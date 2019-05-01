# coding:utf-8
import json
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"hello world!")


def full_game_data(request):
    if request.method == 'GET':
        request_data = dict(request.GET)
        return HttpResponse(json.dumps(request_data, ensure_ascii=False))
    else:
        return HttpResponse('this interface only support get method!')