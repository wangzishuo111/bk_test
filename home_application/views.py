# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from home_application.models import IndexModel
from home_application.hosts import group_hosts, all_hosts, overview
#from home_application.mongo import MongodbClient 

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt

def home(request):
    """
    首页
    """
    overview_info = overview()
    return render(request, 'home_application/home.html', {'info': overview_info})


def contact(request):
    """
    联系我们
    """
    return render(request, 'home_application/contact.html')


def info(request):
    school_info = IndexModel.objects.all()
    return render(request, 'home_application/info.html', {'info': school_info})

def hosts(request):
    all_hosts_list = all_hosts()
    return render(request, 'home_application/hosts.html', {'info': all_hosts_list})

def hosts2(request):
    group_hosts_dic = group_hosts()
    return render(request, 'home_application/hosts2.html', {'info': group_hosts_dic})
