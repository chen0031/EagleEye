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
    sub_str_log_line=log_file_line.split(' ')
    request_path=sub_str_log_line[7]
    request_path_without_params=request_path.split('?')
    transaction=request_path_without_params[0].split('/')
    if len(transaction)>3: 
     transaction_temp=transaction[3]
     #print 'I\'m here '+transaction_name+'\n'
     if transaction_temp.find('servlets')>=0:
        # print request_name.group(1)+'\n'
      #   print transaction_name+'\n'
        transaction_name=transaction_temp.split('.')[4]
        if transaction_name not in request_type_set:
           request_type_set.add(transaction_name)
         
    #     request_parser_handle.write(request_name.group(1)+'\n')
    log_file_line=log_file_handle.readline()
  for index in request_type_set:
      print index
      request_parser_handle.write(index+'\n')     
finally:
  log_file_handle.close()
  request_parser_handle.close()




