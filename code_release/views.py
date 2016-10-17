# -*- coding: UTF-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from controller.public.pagination import *
from controller.core.ansiblehelp import *
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from models import *
from cmdb.models import *
import json

# Create your views here.


def new_template(request):
    # 新增机器页面
    return render_to_response('code_release/new_template.html', locals(), context_instance=RequestContext(request))

def get_servers(request):
    # 获取服务器信息
    response = HttpResponse()
    # server = Server()
    # server.project_name = data['project_name']
    # server.in_ip = data['in_ip']
    # server.ex_ip = data['ex_ip']
    # server.position = data['position']
    # server.save()

    response.write(json.dumps(u'成功'))
    return response