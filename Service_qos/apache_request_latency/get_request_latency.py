#!/bin/python
#The processed log will in the format 'request ip------timestamp-------request name------latency
import os 
import sys
import threading
import numpy as np
import matplotlib.pyplot as plt
import string
log_path=sys.argv[1]
request_config_path='/EagleEye/service_qos/apache_request_latency/request.conf' 
request_list=list()
request_latency_pair=dict()
#latency_list=list{} 
plot_threshold=10000
request_latency_data_path='/EagleEye/service_qos/apache_request_latency/request_latency_data'
request_config_handle=0
request_config_handle=open(request_config_path,'r')
log_handle=open(log_path,'r')
request_latency_data_handle=open(request_latency_data_path,'w')
try:
    request_name=request_config_handle.readline()
    while request_name:
       request_list.append(request_name.strip('\n'))
       # For debug
       print request_name.strip('\n')
       request_name=request_config_handle.readline() 
    print str(len(request_list))
finally: 
       request_config_handle.close()

def draw_graph():
  get_request_latency()
  
  for key in request_latency_pair.keys():
     x_axis=np.linspace(0,len(request_latency_pair[key]),len(request_latency_pair[key]))
   #  x_axis=np.linspace(0,1000,1000)
   #  y_axis=np.linspace(0,1000-10*i,1000)
     y_axis=[]
     for index in request_latency_pair[key]:
        y_axis.append(index)
     plt.plot(x_axis,y_axis,color="red")
    
  plt.show()
      



def get_request_latency():
  log_instance=log_handle.readline()
  while log_instance:
     request_name_in_list=name_in_list(log_instance)
     print request_name_in_list+'\n'
     if len(request_name_in_list)>0:
       sub_str=log_instance.split(' ')
       timestamp=sub_str[3]
       temp_str=sub_str[0]+','+timestamp[1:]+','+request_name_in_list+','+sub_str[10]+'\n'
       request_latency_data_handle.write(temp_str)
       request_latency_data_handle.flush() 
       if request_latency_pair.has_key(request_name_in_list):
          request_latency_pair[request_name_in_list].append(string.atoi(sub_str[10]))
       else:
          latency_list=list()
          request_latency_pair[request_name_in_list]=latency_list
          request_latency_pair[request_name_in_list].append(string.atoi(sub_str[10]))
     log_instance=log_handle.readline() 
   

def name_in_list(instance):
   for index in request_list:
     if instance.find(index)>=0:
       return index
   return ''
def close_file():
   log_handle.close()
   request_latency_data_handle.close()    
if __name__=='__main__':
   draw_graph()   
 
