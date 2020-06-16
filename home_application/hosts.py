from home_application.mongo import MongodbClient 
import collections

con = MongodbClient('10.0.11.148', 27017, 'cmdb', 'cc_HostBase','root', 'eVmA_GTjy6FYJh5HbelU')
hosts_info = con.get_all('cc_HostBase')

def group_hosts():
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
    return hosts_info
    
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

    return group_info
