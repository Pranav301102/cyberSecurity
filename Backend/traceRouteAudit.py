import sys
import scapy.all as scapy
import os
import subprocess
import mongo


print(f"\n-----------Traceroute Scan Started-----------\n")


def traceroute(target):
    print(target)
    if len(sys.argv) == 2:
        target = sys.argv[1]

    ans, unans = scapy.sr(scapy.IP(dst=target, ttl=(
        1, 22), id=scapy.RandShort())/scapy.TCP(flags=0x2), timeout=10)

    result = []
    for snd, rcv in ans:
        if isinstance(rcv.payload, scapy.TCP):
            rambo = "(TCP)"
        else:
            rambo = ""
        hehe = str(snd.ttl) + ". " + str(rcv.src) + " " + str(rambo)
        result.append(hehe)
    return('\n'.join(result))


def audit(foo, id):
    result = traceroute(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})


if __name__ == '__main__':
    print(traceroute('google.com'))
