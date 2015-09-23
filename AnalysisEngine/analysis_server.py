#!/bin/python 
from twisted.web import xmlrpc,server
from twisted.internet import reactor
import os, sys
import time, datetime 
class Worker(xmlrpc.XMLRPC):
   def xmlrpc_test(self):
      print 'This is a test!'
port = 12345
r=Worker(allowNone=True)
if __name__ == '__main__':
  print 'Listening on por', port
  reactor.listenTCP(port,server.Site(r))
  reactor.run()
else: # run the application as a twistd service: twisted -y xmlrpc_server.py
  from twisted.application import service, internet
  application =service.Application('analysis_server')
  reactor.listenTCP(port, server.Site(r))
  reactor.run()
