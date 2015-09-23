#!/bin/python
#import rpy2.robjects as robjects
import array 
#import os
import sys
import rpy2.robjects as robjects
class pca_analysis():
 #  r=robjects.r
 # def __init__(self):
     
  pca_result=''
  r=robjects.r    
  def pca(self,data_path):
      # return_value=dict()
      # r=robjects.r
      # read_param='%s,header=FALSE' %(data_path)
       raw_data=pca_analysis.r['read.table'](data_path)
      # data_matrix=r.matrix(raw_data)
      # pca_result=r.princomp('~CPU.User+CPU.Sys+CPU.ProcQue+MEM.Used+MEM.PageFaults+SOCK.Used+NET.RxPktTot',raw_data,cor = 'TRUE') 
       pca_analysis.pca_result=pca_analysis.r.princomp(raw_data,cor='TRUE')
      # return pca_result
  def draw_pca(self,data_path):
      # read_param=data_path+','+'head=FALSE'
       pca_analysis.pca_result=self.pca(data_path)
      # r=robjects.r
       #print r.loadings(pca_result)
       #print r.summary(pca_result)
       pca_analysis.r.X11()
       pca_analysis.r.par(mfrow=array.array('i',[1,2]))
       pca_analysis.r.plot(pca_analysis.pca_result,main='Eigen value')
       pca_analysis.r.biplot(pca_analysis.pca_result,main='biplot')
       if sys.stdin.readline()=="quit" :
         sys.exit(0)
  def return_loadings(self):
      return pca_analysis.r.loadings(pca_analysis.pca_result)
  def return_summary(self):
      return pca_analysis.r.summary(pca_analysis.pca_result)
  
