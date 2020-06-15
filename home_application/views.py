# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from home_application.models import IndexModel
from home_application.mongo import MongodbClient 

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt

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


def info(request):
    #school_info = IndexModel.objects.get(id=1)
    school_info = IndexModel.objects.all()
    return render(request, 'home_application/info.html', {'info': school_info})

def hosts(request):
    con = MongodbClient('10.0.11.148', 27017, 'cmdb', 'cc_HostBase','root', 'eVmA_GTjy6FYJh5HbelU')
    hosts_info = con.get_all('cc_HostBase')
    return render(request, 'home_application/hosts.html', {'info': hosts_info})

def hosts2(request):
    con = MongodbClient('10.0.11.148', 27017, 'cmdb', 'cc_HostBase','root', 'eVmA_GTjy6FYJh5HbelU')
    hosts_info = con.get_all('cc_HostBase')
    dic = {}
    data = [info for info in hosts_info if info.get('bk_group')== 'Data']
    server = [info for info in hosts_info if info.get('bk_group')== 'Server']
    none = [info for info in hosts_info if info.get('bk_group')== None]
    infra = [info for info in hosts_info if info.get('bk_group')== 'Infrastructure']
    dic['data'] = data
    dic['server'] = server
    dic['infra'] = infra
    dic['none'] = none
    return render(request, 'home_application/hosts2.html', {'info': dic})
