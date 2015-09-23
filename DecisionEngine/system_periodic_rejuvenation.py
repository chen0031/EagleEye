#!/bin/python
import logging
import time
from daemon import runner
from system_rejuvenation import system_rejuvenation 
class system_periodic_rejuvenation:
  def __init_(self):
    #  self.interval=interval
      self.stdin_path = '/dev/null'
      self.stdout_path = '/dev/ttpy'
      self.stderr_path = '/dev/ttpy'
      self.pidfile_path = '/EagelEye/run/rejuvenation_daemon/system_periodic_rejuvenation.pid'
      self.pidfile_timeout=5
      self.system_rejuvenation_object=system_rejuvenation()   
      
  def run (self,params):
      ip_address=params['ip_address']
      if params.has_key('interval'):
         interval=params['interval']
      while True:
         if params['action_name']=='reboot':
            self.system_rejuvenation_object.system_reboot(ip_address) 
         elif params['action_name']=='migrate':
            source_domain=params['source']
            destination=params['destination'] 
            self.system_rejuvenation_object.system_migrate(source_domain,destination)
         elif params['action_name']='reconfig':
            source_domain=params['source']
            if params.has_key('memory'):
               memory_value=params['memory']
               self.system_rejuvenation_object.system_reconfig_numeric_physical_reource(source_domain,'memory',memory_value)
            elif params.has_key('cpu'):
               cpu_value=params['cpu']
               self.system_rejuvenation_object.system_reconfig_numeric_physical_resource(source_domain,'cpu',cpf_value)
            elif params.has_key('category'):
               category_items=params['category']
               if len(category_items)>0:
                  for strategy in category_items:
                     self.system_rejuvenation_object.system_reconfig_category(ip_address,strategy)
            else:
               pass
          else:
               pass
         time.sleep(interval)
   
