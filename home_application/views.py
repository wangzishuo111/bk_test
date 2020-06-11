# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from home_application.models import *

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt

def hello(request):
    return redirect('http://zabbix.infra.growingio.com/zabbix.php?action=dashboard.view')

def home(request):
    """
    首页
    """
    return render(request, 'home_application/home.html')


def contact(request):
    """
    联系我们
    """
    return render(request, 'home_application/contact.html')

def listinfo(request):
    users = IndexModel.objects.all()
    return render(request, 'home_application/listinfo.html', {'users': users}) 
