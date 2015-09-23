#!/bin/python 
import logging 
import time 
from  daemon import runner
from  system_rejuvenation import system_rejuvenation
from  service_rejuvenation import service_rejuvenation
from  process_rejuvenation import process_rejuvenation
from  xml.etree.ElementTree import ElementTree
from  xml.etree.ElementTree import Element
from  xml.etree.ElementTree import SubElement
from  xml.etree.ElementTree import dump
from  xml.etree.ElementTree import Comment
from  xml.etree.ElementTree import toString
 
class rejuvenation_daemon():
  def __init__(self,interval,analysis_result,rejuvenation_level):
     self.stdin_path = '/dev/null'
     self.stdout_path = '/dev/tty'
     self.stderr_path = '/dev/tty'
     self.pidfile_path = '/EagleEye/run/rejuvenation_daemon/rejuvenation_daemon.pid'
     self.pidfile_timeout=5
     self.scan_interval=interval
     self.analysis_result=analysis_result
     self.rejuvenation_level=rejuvenation_level
     self.xml_doc=ElementTree.parse(self.analysis_result)
  def rejuvenation_strategy(self):
     i=1
  def system_actions(self):
     doc_root=self.xml_doc.getroot()
     for level in doc_root:
       
     ip_address=system_actions.Element
  def service_actions(self):
     i=1
  def process_actions(self):
     i=1
  def run(self):
     while True:
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warn("Warning message")
        time.sleep(5)
rejuvenation_daemon=rejuvenation_daemon()
logger=logging.getLogger("DaemonLog")
logger.setLevel(logging.ERROR)
formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler=logging.FileHandler("/EagelEye/log/rejuvenation_daemon/rejuvenation_daemon.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

daemon_runner=runner.DaemonRunner(rejuvenation_daemon)
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()

