# scan a range of port numbers on a host concurrently
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from concurrent.futures import ThreadPoolExecutor
import os
import subprocess
import mongo
print("\n-----------Remote Port Scanner Started-----------")
def scanner(hostname):
    host = hostname
    port = range(1024)
    # returns True if a connection can be made, False otherwise
    def test_port_number(host, port):
        # create and configure the socket
        with socket(AF_INET, SOCK_STREAM) as sock:
            # set a timeout of a few seconds
            sock.settimeout(3)
            # connecting may fail
            try:
                # attempt to connect
                sock.connect((host, port))
                # a successful connection was made
                return True
            except:
                # ignore the failure
                return False
    
    # scan port numbers on a host
    def port_scan(host, ports):
        print(f'\nPort Scanning {host}...')
        # create the thread pool
        with ThreadPoolExecutor(len(ports)) as executor:
            # dispatch all tasks
            results = executor.map(test_port_number, [host]*len(ports), ports)
            # report results in order
            result = []
            for port,is_open in zip(ports,results):
                if is_open:
                    hehe = (f'{port}')
                    result.append(hehe)
        return(result)
    return(port_scan(host, port))


def audit(foo, id):
    result = scanner(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})
    
    
if __name__ == '__main__':
    print(scanner('atharvacoe.ac.in'))


