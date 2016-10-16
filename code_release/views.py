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
import json

# Create your views here.


def new_template(request):
    # 新增机器页面
    return render_to_response('code_release/new_template.html', locals(), context_instance=RequestContext(request))
