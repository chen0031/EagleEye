#!/bin/python 
import os
import sys
import re
log_path=sys.argv[1]
log_file_handle=open(log_path,'r')
request_parser_file='/EagleEye/service_qos/apache_request_latency/request_parser_file'
request_parser_handle=open(request_parser_file,'w')
request_type_set=set([])
try:
  log_file_line=log_file_handle.readline()
  while log_file_line:
     regex_request=re.compile('.*/(.*)\.php.*')
     print 'I\'m here\n'
     request_name=regex_request.match(log_file_line)
     if request_name:
        # print request_name.group(1)+'\n'
         if request_name.group(1) not in request_type_set:
            request_type_set.add(request_name.group(1))
         
    #     request_parser_handle.write(request_name.group(1)+'\n')
     log_file_line=log_file_handle.readline()
  for index in request_type_set:
      request_parser_handle.write(index+'\n')     
finally:
  log_file_handle.close()
  request_parser_handle.close()




