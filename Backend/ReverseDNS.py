import socket
import os
import subprocess
import mongo
print("\n-----------Reverse DNS Scanner Started-----------\n")
def reverse_dns(hostname):
  try:
    hostip = socket.gethostbyname(hostname.strip())
    hehe1 = "Domain Name: "+hostname
    hehe2 = "IP Address: "+hostip

    def get_domain_name(ip_address):
      result=socket.gethostbyaddr(ip_address)
      return list(result)[0]
    # print("Domain name using PTR DNS:")
    hehe3 = "Reverse DNS address: "+get_domain_name(hostip)
    return (str(hehe1) +"\n"+ str(hehe2) +"\n"+ str(hehe3))
  except socket.herror:
    hehe = "\nCould not find results for reverse DNS search!!!"
    return (hehe)
    
def audit(foo, id):
    result = reverse_dns(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})
    
    
if __name__ == '__main__':
  host = 'atharvacoe.ac.in'
  ip = socket.gethostbyname(host.strip())
  print(reverse_dns(host, ip))

  
