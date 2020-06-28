from mongo import MongodbClient 
import collections


con = MongodbClient('10.0.11.148', 27017, 'cmdb', 'cc_HostBase','root', 'eVmA_GTjy6FYJh5HbelU')

def group_hosts():
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
    return dic

def all_hosts():
    hosts_info = con.get_all('cc_HostBase')
    return hosts_info
    
def overview():
    hosts_info = con.get_all('cc_HostBase')
    info = []
    for host_info in hosts_info:
        info.append((host_info.get("bk_group"), host_info.get("bk_type")))

    d = collections.defaultdict(list)
    for k, v in info:
        d[k].append(v)
    
    group_info = dict(d.items())
    for k, v in group_info.items():
        group_info[k] = dict(collections.Counter(v))
    return group_info

def resource():
    hosts_info = con.get_all('cc_HostBase')
    info = []
    ret = []
    for host_info in hosts_info:
        info.append((host_info.get("bk_group"), host_info.get("bk_cpu")))

    d = collections.defaultdict(list)
    for k, v in info:
        d[k].append(v)

    group_info = dict(d.items())
    for k, v in group_info.items():
        ret.append((k,sum(v)))
    print (ret)
    return ret

def resources():
    hosts_info = con.get_all('cc_HostBase')
    info_cpu = []
    info_mem = []
    ret_cpu = []
    ret_mem = []
    for host_info in hosts_info:
        print (host_info)
        info_cpu.append((host_info.get("bk_group"), host_info.get("bk_cpu")))
        info_mem.append((host_info.get("bk_group"), host_info.get("bk_mem")))

    d = collections.defaultdict(list)
    for k, v in info_cpu:
        d[k].append(v)
    group_cpu = dict(d.items())
    for k, v in group_cpu.items():
        ret_cpu.append((k,sum(v)))

    x = collections.defaultdict(list)
    for k, v in info_mem:
        x[k].append(v)
    group_mem = dict(x.items())
    for k, v in group_mem.items():
        ret_mem.append((k,sum(v)))

    return ret_cpu, ret_mem

resources()
