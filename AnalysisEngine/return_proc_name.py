#!/bin/python
from look_up_netif_info import look_up_netif_info
import os
import sys
work_dir='/EagleEye'
netIF='ssh'
proc_name_look_up=look_up_netif_info(netIF,work_dir)
proc_name=proc_name_look_up.ret_process_name(netIF)
if proc_name=='':
  print 'There is something wrong to open the proc_file!'
else:
  print proc_name


#print 'hello world' 
