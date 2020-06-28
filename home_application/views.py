# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from home_application.models import IndexModel
from home_application.hosts import group_hosts, all_hosts, overview, resource
#from home_application.chart import chart_table 
#from home_application.mongo import MongodbClient 



from django.shortcuts import render
from django.http import HttpResponse

from matplotlib.figure import Figure                      
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

import random
import datetime


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

def chart(request):
    import numpy as np
    import base64
    import matplotlib.pyplot as plt
    from io import BytesIO

    #[('Infrastructure', 226), ('QA', 112), ('CDP', 8), ('Server', 162), ('Data', 3026), ('Platform', 56), ('IT', 7), ('AdsTracking', 2), ('AdsTrack', 8)]
    cpus, mems = resource()
    cpu_names = []
    cpu_values = []
    mem_names = []
    mem_values = []

    for cpu in cpus:
        cpu_names.append(cpu[0])
        cpu_values.append(cpu[1])

    for mem in mems:
        mem_names.append(mem[0])
        mem_values.append(mem[1])
    
    x =list(i *4 for i in range(len(cpu_names)))
    total_width, n = 3.2, 2
    width = total_width / n
    rects1 = plt.bar(x, cpu_values, width=width, label='cpu',fc = 'y')
    for i in range(len(x)):
        x[i] = x[i] + width
    rects2 = plt.bar(x, mem_values, width=width, label='mem',tick_label = mem_names,fc = 'r')
    plt.legend()
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
    for rect in rects2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
        
    buffer = BytesIO()
    plt.savefig(buffer)
    plot_data = buffer.getvalue()
    imb = base64.b64encode(plot_data)
    ims = imb.decode()
    imd = "data:image/png;base64," + ims
    context = {
            'info': imd,
        }
    plt.close()
    return render(request, 'home_application/chart.html', context)
