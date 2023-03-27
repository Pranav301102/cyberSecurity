import mongo
import time


# define a function like this to be called inside the audit function
def ssl_audit(domain):
    # placeholder
    time.sleep(10)

    return domain + " pinged successfully"


def audit(foo, id):
    result = ssl_audit(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})
    

if __name__ == '__main__':
    print(ssl_audit('google.com'))
