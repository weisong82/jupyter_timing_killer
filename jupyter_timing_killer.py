
# coding: utf-8

# 根据设定的运行时间，清理jupyter notebook进程。 避免过多的note打开一直占用系统资源
# 
# 测试环境： 
# psutil  5.4.3 (在5.0.x版本后出现了psutil.process_iter函数的参数变化，会报错，建议升级版本或者修改代码 )
# python3.6    

# In[ ]:


import psutil
import os
import time
#http://psutil.readthedocs.io/en/latest/#


# In[ ]:


#time interval to kill in seconds
time2die = 3 * 3600  #3hour


# In[ ]:


'''
cmdline 匹配进程id list  notebook的cmd是这样的，匹配'ipykernel_launcher'正合适.  字符串部分包含需要改改if条件咯

['/root/miniconda3/bin/python',
 '-m',
 'ipykernel_launcher',
 '-f',
 '/run/user/0/jupyter/kernel-5c2390e6-55d8-4858-9162-1b90dd58132d.json']

'''
def match_procs_by_cmdline(cmd):
    ls = []
    for p in psutil.process_iter(attrs=["pid",'cmdline']):
        if p.info['cmdline'] and ( cmd in p.info['cmdline'])  :
            ls.append(p.info['pid'])
    return ls


# In[ ]:


'''

check string against Process.name(), Process.exe() and Process.cmdline():

'''
def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
        if name == p.info['name'] or                 p.info['exe'] and os.path.basename(p.info['exe']) == name or                 p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls


# In[ ]:


notes=match_procs_by_cmdline('ipykernel_launcher')
print("check in : %s" %(notes))


# In[ ]:


for n in notes:
    p = psutil.Process(n)
    if(time.time() - p.create_time()  >= time2die):
        p.terminate()
        print("time to die for pid: %s  cmd: %s" %( n ,p.cmdline() ) )

