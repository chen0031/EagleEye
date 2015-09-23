#!/bin/python
import os
import sys
from look_up_netif_info import look_up_netif_info 
#from xmlrpclib 
service_dependency_dir='/EagleEye/service_dep/'
shell_dir='/EagleEye/shell/'
work_dir='/EagleEye'
#source_info=list();
#destination_info=list();
#Get the connection information among different ip+port
cmd_connection=shell_dir+'ConnectionInfo.sh'
raw_connection_file_path=service_dependency_dir+'Connection.tmp'
transfered_connection_file_path=service_dependency_dir+'transfered_connection.tmp'
#Get the process name with respective port
cmd_get_procname_by_port=shell_dir+'getProcNameByNetworkInterface.sh'
os.system(cmd_connection)
if os.path.exists(raw_connection_file_path):
  raw_connection_handle=open(raw_connection_file_path,'r')
  transfered_connection_handle=open(transfered_connection_file_path,'w')
  try:
    raw_connection_instance=raw_connection_handle.readline()
    while raw_connection_instance:
       source_info=list()
       destination_info=list()
       sub_string=raw_connection_instance.split(' ')
#      Get the source information 
       source_sub_string=sub_string[1].split(':')
       source_ip=source_sub_string[0]
       source_port=source_sub_string[1]
       source_info.append(source_ip);       
#      Get the source process name from shell script
#      cmd_get_procname_by_port_with_port=cmd_get_procname_by_port+' '+source_port
#      os.system(cmd_get_procname_by_port_with_port)
#      Get the process name from look_up_netif_info       
       get_process_name=look_up_netif_info(source_port,work_dir)
       source_process_name=get_process_name.ret_process_name(source_port)
       source_info.append(source_process_name)
       source_info.append(source_port)
#      Get the destination information   
       destination_sub_string=sub_string[2].split(':')
       destination_ip=destination_sub_string[0]
#       if (cmp(destination_ip,source_ip)!=0):
#        remote_call=serverproxy(".....")
#         print 'We need to inquire the information from remote machine\n'
#       else:
       destination_port=destination_sub_string[1]
       destination_info.append(destination_ip)
       destination_process_name=get_process_name.ret_process_name(destination_port)
       destination_info.append(destination_process_name)
       destination_info.append(destination_port)
       transfered_connection_instance=','.join(source_info)+' '+','.join(destination_info)
       transfered_connection_handle.write(transfered_connection_instance)
       transfered_connection_handle.write('\n')
       raw_connection_instance=raw_connection_handle.readline()
  finally:
    raw_connection_handle.close()
    transfered_connection_handle.close()
else:
  print 'We need to execute the shell script again to get the connection information\n'
  os.system(cmd_connection)

