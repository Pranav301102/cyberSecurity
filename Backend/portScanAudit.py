import mongo
import time


# define a function like this to be called inside the audit function
def port_scan(domain):
    # placeholder
    time.sleep(10)

    return domain + " pinged successfully"


def audit(foo, id):
    result = port_scan(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})
    
    
if __name__ == '__main__':
    print(port_scan('google.com'))
