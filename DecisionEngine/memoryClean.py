#!/bin/python
#system memory reclaim using drop_caches
class memoryClean:
  def __init__(self,ip_address):
    self.work_path='/EagleEye/shell'  
    self.ip_address=ip_address
  def run(self):
    command_string=self.work_path+'/'+'memoryClean.sh'+' '+self.ip_address
    if (os.system(command_string)) == 0:
       return 1
    else:
       return 0

