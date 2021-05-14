import os
from datetime import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from AutoPPTServer import information_store
from AutoPPTServer.settings import BASE_DIR
from api.AutoPPTCut import Server
from api.models import Template, User
from api.serializers import TemplateSerializers
from api.utils import Information
import json


class LoginView(APIView):
    def post(self, request):
        json_data = json.loads(request.body.decode("utf-8"))
        username = json_data['username']
        if True:
            if User.objects.filter(username=username):
                user = User(username=username)
                user.save()
            response = HttpResponse("Login OK")
            response.set_signed_cookie("username", username, salt='salt')
            return response
        else:
            return HttpResponse("Login Failed")


class TemplatesView(APIView):
    def get(self, request):
        username = request.get_signed_cookie('username', salt="salt")
        if User.objects.filter(username=username):
            return HttpResponse("Failed")

        templates = Template.objects.all()
        serializer = TemplateSerializers(templates, many=True)
        return Response(serializer.data)


class UploadView(APIView):
    def post(self, request):
        username = request.get_signed_cookie('username', salt="salt")
        if User.objects.filter(username=username):
            return HttpResponse("Failed")

        file = request.FILES.get("file", None)
        if not file:
            return HttpResponse("-1")
        save_file = open(os.path.join(BASE_DIR, 'file\\' + file.name), 'wb+')
        for chunk in file.chunks():
            save_file.write(chunk)
        save_file.close()
        return HttpResponse(os.path.join(BASE_DIR, 'file\\' + file.name))


class InformationView(APIView):
    def post(self, request):
        username = request.get_signed_cookie('username', salt="salt")
        if User.objects.filter(username=username):
            return HttpResponse("Failed")

        json_data = json.loads(request.body.decode("utf-8"))
        title = json_data['title']
        page_num = json_data['page_num']
        cut_num = json_data['cut_num']
        template_id = json_data['template_id']
        file_url = json_data['file_url']
        information = Information(title, page_num, cut_num, template_id, file_url)

        ppt_maker = Server()
        list1, list2 = ppt_maker.getLogicCut(file_url, cut_num)
        information.set_logic_cut(cut_num, list1, list2)

        information_store.save(username, information)

        return JsonResponse(information.to_dict(), safe=False)


class DisplayView(APIView):
    def post(self, request):
        username = request.get_signed_cookie('username', salt="salt")
        if User.objects.filter(username=username):
            return HttpResponse("Failed")

        information = information_store.get(username)

        json_data = json.loads(request.body.decode("utf-8"))
        data = json_data['summary']
        information.cut_num = len(data)
        information.summary = data
        page_num = information.page_num
        information_store.save(username, information)

        logic_cut_list, summary = information.get_logic_cut()

        ppt_maker = Server()
        display_list = ppt_maker.getDisplayCut(logic_cut_list, page_num)

        return JsonResponse(display_list, safe=False)


class GetPPTView(APIView):
    def post(self, request):
        username = request.get_signed_cookie('username', salt="salt")
        if User.objects.filter(username=username):
            return HttpResponse("Failed")

        information = information_store.get(username)

        json_data = json.loads(request.body.decode("utf-8"))
        data = json_data['display']
        logic_cut, summary = information.get_logic_cut()
        display_cut = data
        page_num = information.page_num
        title = information.title
        template = Template.objects.get(id=information.template_id)
        template_path = template.template_url
        dst_path = username+"\\"+str(int(time.time))+".pptx"
        dst_name = os.path.join(BASE_DIR,dst_path)
        ppt_maker = Server()
        ppt_maker.makePPT(logic_cut, display_cut, page_num, title, template_path, dst_name)

        return "127.0.0.1:8000/"+dst_path.replace('\\', '/')
