#!/bin/python
import os
import sys
class look_up_netif_info:
  _netif='' 
  def  __init__(self,netif,work_dir):
     self.netif=netif
     self.work_dir=work_dir
#     look_up_netif_info._netif=netif 
  
  def ret_process_name(self,netif):
     process_name=''
     if os.path.exists(self.work_dir):
       cmdLine=self.work_dir+'/shell'+'/'+'getProcNameByNetworkInterface.sh'+' '
       cmdLineParam=netif
       combindedCmd=cmdLine+cmdLineParam
       os.system(combindedCmd)
     #  os.popen(combindedCmd)    
       proc_file_path=self.work_dir+'/service_dep'+'/'+'processName.tmp'
     #  print proc_file_path
       if os.path.exists(proc_file_path):
          proc_file=open(proc_file_path,'r')
          try:
       #    proc_file=open(proc_file_path,'r')
       #    proc_file=open(proc_file_path,'r')
            process_name=proc_file.readline()
            return process_name.strip('\n')
          finally:
            proc_file.close()
         #  print 'There is something wrong to open the proc_file\n' 
       else: 
         print 'Please check the executed shell command!\n'
         return ''
  
