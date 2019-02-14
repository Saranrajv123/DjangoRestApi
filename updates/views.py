from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update
from django.views.generic import View
from django.core.serializers import serialize
import json

from restapi.mixins import JsonResponseMixin
# Create your views here.

def json_example_view(request):
    '''
    URI - or Rest api
    GET - Method
    '''

    data = {
        "content": 'Some Contents',
        "count": 1000,
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type="application/json")
    # return JsonResponse(data)


class Json_CBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "content": 'some Content',
            "count": 5000,
        }
        return JsonResponse(data)
    

class Json_CBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "content": 'some Content',
            "count": 5000,
        }
        return self.render_to_json_response(data)

class serializedDetailView(View):
    def get(self,request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        # serialze_data = serialize('json', [obj,], fields=['user', 'content'])
        # data = {
        #     "user": obj.user.username,
        #     "content": obj.content,
        # }
        # json_data = serialze_data
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request,*args, **kwargs):
        return HttpResponse({}, content_type='application/json')
    
    def put(self, requests, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')


class serializedListView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.all()
        json_data = Update.objects.all().serialize()
        # serialize_data = serialize('json', obj, fields=('user', 'content'))
        # json_data = serialize_data
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        data = json.dumps({"dummy": 'unknowndata'})
        return HttpResponse(data, content_type='application/json')
