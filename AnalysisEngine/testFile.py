#!/bin/python
from  service_topology_graph  import Draw_service_graph 
if __name__=='__main__':
  #service_dep_file_path='/EagleEye/service_dep/transfered_connection.tmp'
  service_dep_file_path='/EagleEye/service_dep/metric_dependency.tmp'
  graph=Draw_service_graph(service_dep_file_path)
  graph.draw()
