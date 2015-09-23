from twisted.internet import reactor,protocol,defer  
from twisted.application import service,internet  
from twisted.python import log  
  
def main():  
    print 'started!'  
    return  
  
if __name__=='__main__':  
    main()  
elif __name__=='__builtin__':  
    main()  
    application=service.Application('hello')  
