from pythonping import ping
import socket
import os
import subprocess
import mongo

print("\n-----------Host Service Detection-----------\n")
def ping1(hostname):
    try:
        hehe0 = "Host status for: "+ hostname
        ip_address = socket.gethostbyname(hostname.strip())
        hehe1 = "IP Address: "+ str(ip_address)
        response_list = ping(ip_address, size=40, count=10)
        if response_list.rtt_avg_ms > 0:
            hehe2 = "Host is UP!"
        else:
            hehe2 = "Host is DOWN!"
        hehe3 = ("Ping Avg Response Time: "+ str(response_list.rtt_avg_ms))
        return (str(hehe0)  +"\n"+  str(hehe1) +"\n"+ str(hehe2) +"\n"+ str(hehe3))
    except socket.gaierror:
        hehe1 = "Hostname " +hostname+ " is unavailable or check your internet!"
        return(hehe1)

def audit(foo, id):
    result =ping1(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})
    
        
if __name__ == '__main__':
    print(ping1('netflix.com'))

