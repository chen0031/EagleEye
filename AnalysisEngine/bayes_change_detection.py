#!/bin/sh
import os
import sys
import Image
import matplotlib.pyplot as plt
import rpy2.robjects as robjects
#import numpy
class bayes_change:
  def __init__(self,data_path):
     self.data_path=data_path
     self.bcp_result_data='/EagleEye/temp/bcp_result.dat'
     self.bcp_result_image='/EagleEye/temp/bcp_result.jpeg'
     self.bcp_result_filter='/EagleEye/shell/parseBcpResult.sh'
     self.bcp_filtered_result='/EagleEye/temp/bcp_result_single_column.dat'
     self.r=robjects.r
     self.raw_data=[]
     
  def change_detection(self,metric_name):
     data_handle=open(self.data_path,'r')
     try:
       header=data_handle.readline().strip('\n')
       header_item=header.split(' ')
       i=1
       for item in header_item:
          if item == metric_name:
             break
          i=i+1  
       print i    
       command_string='R --save --args %s %d < /EagleEye/R/bcp.R' % (self.data_path,i)
       os.system(command_string)
     finally:
       data_handle.close() 
  def draw_graph(self,image):
     command_string=self.bcp_result_filter+' '+self.bcp_result_data
     os.system(command_string)
     
     if os.path.exists(self.bcp_filtered_result):
      # bcp_filtered_result_data=self.r['read.table'](self.bcp_filtered_result)
       
      # bcp_filtered_result_data_no_tail=bcp_filtered_result_data[1:len(bcp_filtered_result_data)-1]
       if image==1:
         bcp_result = Image.open(self.bcp_result_image)
         bcp_result.show()
       elif image==2:
         plt.subplot(211)
         plt.plot(range(0,len(bcp_filtered_result_data_no_tail),1),bcp_filtered_result_data_no_tail,'r-')
         plt.show()
       else:
         print 'Set the parameter image type\n'
         sys.exit(0)
     else:
       print 'There is no bcp result\n'
   #  we will give two drawing methods 'image=1' represents getting from R script 
   #    {
   #      1:lambda:{ bcp_result = Image.open(self.bcp_result_image);bcp_result.show()},
                  
   #      2:lambda:{ plt.subplot(2 1 1);plt.plot(numpy.range(0,len(bcp_filtered_result_data_no_tail),1),bcp_filtered_result_data_no_tail,'r-') }
                   # plt.subplot(2 1 2)
                   # plt.plot(numpy.range(                          
                  
   #    }[image]()
   #    
   # def parse_bcp_result(self):
   #   os.system(self.bcp_result_filter)  
       
