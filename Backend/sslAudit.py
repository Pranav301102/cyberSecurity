import ssl
import socket
import datetime
import boto3
import os
import subprocess
import mongo

client = boto3.client("ses", region_name="us-east-1")

print(f"\n-----------SSL Status Service Started-----------\n")


def sslcert(hostname):
    host = hostname
    # port= input ("Enter Port (80, 8080, 443): ")
    port = '443'
    try:
        hehe0 = f"Checking certifcate for: {host}"
        context = ssl.create_default_context()
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                certificate = ssock.getpeercert()
            certExpires = datetime.datetime.strptime(
                certificate["notAfter"], "%b %d %H:%M:%S %Y %Z"
            )
            daysToExpiration = (certExpires - datetime.datetime.now()).days
            hehe1 = f"Expires on: {certExpires} in {daysToExpiration} days"
        return (hehe0 + '\n' + hehe1)

    except Exception as e:
        print(e)
        hehe = f"Error on connection to Server or incorrect port selected for: {host}"
        return (hehe)


def audit(foo, id):
    result = sslcert(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})


if __name__ == '__main__':
    print(sslcert('google.com'))
