import mongo
import time


def audit(foo, id):
    # placeholder
    time.sleep(10)
    result = foo['domain'] + " is a foo"

    # updating in db
    mongo.db.foo.update_one(
        {'_id': id}, {"$set": {"completed": True, "result": result}})
