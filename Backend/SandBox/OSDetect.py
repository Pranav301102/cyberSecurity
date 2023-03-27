# Run As Admin
import mongo
import time
import nmap
import socket
import os
import subprocess

def osDetect(hostname):
    print('\n-----------Remote OS Detection Started-----------\n')
    try:
        hostip = socket.gethostbyname(hostname)
        nm = nmap.PortScanner()
        machine = nm.scan(hostip, arguments='-O')
        hehe1 = "OS Type: "+ str(machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['osfamily'])
        hehe2 = "Detection Accuracy: "+ str(machine['scan'][str(hostip)]['osmatch'][0]['osclass'][0]['accuracy'])
        results = (hehe1 +'\n'+ hehe2)
        return (results)
        
    except IndexError:
        return("Cannot detect host OS for: "+ hostname)
    
def audit(foo, id):
    result = osDetect(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})
    
        
if __name__ == '__main__':
    print(osDetect('atharvacoe.ac.in'))