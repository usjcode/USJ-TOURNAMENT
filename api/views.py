from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.


def api_view(request, *args, **kwargs):
    # request => HttpRequest
    print (request.body) # byte string
    data = json.loads(request.body)
    pre_data = json.dumps(data)
    data['headers']= dict(request.headers)
    data['params']= dict(request.GET)
    data['post-data'] = dict(request.POST)
    print (data)
    # data['headers'] = dict (request.headers)
    # data['content-type'] = (request.content_type)
    print (request.headers) 
    return JsonResponse(data)