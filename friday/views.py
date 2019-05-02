# coding:utf-8
import json
from django.http import HttpResponse
from service.thor.src.thor_v1 import main as get_game_data

def index(request):
    return HttpResponse(u"hello world!")


def full_game_data(request):
    if request.method == 'GET':
        # todo check the auth of request
        # request_data = dict(request.GET)
        game_data = get_game_data()
        return HttpResponse(json.dumps(game_data, ensure_ascii=False))
    else:
        return HttpResponse('this interface only support get method!')