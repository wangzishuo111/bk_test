# -*- coding: utf-8 -*-
# from django.test import TestCase

# Create your tests here.

from mongo import MongodbClient

con = MongodbClient('10.0.11.148', 27017, 'cmdb', 'cc_HostBase','root', 'eVmA_GTjy6FYJh5HbelU')
hosts_info = con.get_all('cc_HostBase')
for host_info in hosts_info:
    print (host_info.get('bk_host_name'), host_info.get('bk_host_innerip'), host_info.get('bk_group'))
