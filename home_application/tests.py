# -*- coding: utf-8 -*-


from mongo import MongodbClient
import collections

con = MongodbClient('10.0.11.148', 27017, 'cmdb', 'cc_HostBase','root', 'eVmA_GTjy6FYJh5HbelU')
hosts_info = con.get_all('cc_HostBase')

#info = []
#
#for host_info in hosts_info:
#    info.append((host_info.get("bk_group"), host_info.get("bk_type")))
#
#d = collections.defaultdict(list)
#for k, v in info:
#    d[k].append(v)
#
#group_info = dict(d.items())
#for k, v in group_info.items():
#    group_info[k] = collections.Counter(v)
#
#for k, v in group_info.items():
#    print (k)
#    print (v)

def overview():
    info = []
    for host_info in hosts_info:
        info.append((host_info.get("bk_group"), host_info.get("bk_type")))

    d = collections.defaultdict(list)
    for k, v in info:
        d[k].append(v)

    group_info = dict(d.items())
    for k, v in group_info.items():
        group_info[k] = dict(collections.Counter(v))

    print (group_info)

def all_hosts():
    return hosts_info

print (all_hosts())
