import mongo
import time


# define a function like this to be called inside the audit function
def trace_route(domain):
    # placeholder
    time.sleep(10)

    return domain + " pinged successfully"


def audit(foo, id):
    result = trace_route(foo['domain'])

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})


if __name__ == '__main__':
    print(trace_route('google.com'))
