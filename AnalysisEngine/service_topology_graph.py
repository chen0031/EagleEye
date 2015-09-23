#!/bin/python 
from networkx import graphviz_layout
import networkx as nx
import matplotlib.pyplot as plt
import os
import sys 
class Draw_service_graph():
  def __init__(self,service_dep_file_path):
     self.service_dep_file_path=service_dep_file_path
  def draw(self):
     if os.path.exists(self.service_dep_file_path):
       graph=nx.DiGraph()
       service_dep_file_handle=open(self.service_dep_file_path,'r')
       try:
      
          raw_connection_instance=service_dep_file_handle.readline()
          while  raw_connection_instance:
             connection_instance=raw_connection_instance.strip('\n')
             sub_str=connection_instance.split(' ')
             source_sub_str=sub_str[0]
             destination_sub_str=sub_str[1]
             localhost=sub_str[0].split(',')
             if len(destination_sub_str)==0:
                 destination_sub_str='remote process'
             graph.add_node(source_sub_str)
             graph.add_node(destination_sub_str)
             graph.add_edge(source_sub_str,destination_sub_str)
             graph.add_edge(source_sub_str,localhost[0])
             raw_connection_instance=service_dep_file_handle.readline()
#         Set the attributes of the grpah  
 #         pos=nx.spring_layout(graph,dim=2,iterations=5)
          pos=nx.graphviz_layout(graph,prog='dot')
          nx.draw(graph,pos,edge_color='b',font_size=15)
          
          plt.show()
       finally:
          service_dep_file_handle.close()
     

