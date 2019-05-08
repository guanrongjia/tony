# coding:utf-8
import json
from django.shortcuts import render
from django.http import HttpResponse
from serivices.thor.src.thor_v1 import main as get_game_data



def index(request):
    return render(request, 'index.html')


def full_game_data(request):
    if request.method == 'GET':
        # todo check the auth of request
        # request_data = dict(request.GET)
        game_data = get_game_data()
        return HttpResponse(json.dumps(game_data, ensure_ascii=False))
    else:
        return HttpResponse('this interface only support get method!')