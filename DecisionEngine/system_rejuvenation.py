#!/bin/python
import os,sys
import importlib
class system_rejuvenation:
 def __init__(self,analysis_result_path):
     self.analysis_result_path=analysis_result_path
 def system_reboot(self,ip_address):
     command_string='/EagleEye/shell/systemReboot.sh'+' '+ip_address
     os.system(command_string)
 def system_migrate(self,source,destination):
     command_string='/EagleEye/shell/systemMigrate.sh'+' '+source+' '+destination
     os.system(command_string)
 def system_reconfig_numeric_physical_resource(self,source,metric,value)
     command_string='/EagleEye/shell/systemPhysicalResource.sh'+' '+source+' '+metric+' '+'%d' % value
     os.system(command_tring)
 def system_reconfig_numeric_logical_resource(self,ip_address,metric,value)
     command_string='/EagleEye/shell/systemLogicalResource.sh'+' '+ip_address+' '+metric+' '+'%d' % value
     os.system(command_string)
 def system_reconfig_category(self,ip_address,strategy)
     module_name=importlib.import_module(strategy)
     class_object=getattr(module_name,strategy)
     class_instance=class_object(ip_address)
     return_flag=class_instance.run()
     return return_flag
     
      
       
