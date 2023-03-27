from fastapi import FastAPI
from bson.objectid import ObjectId
import threading
import mongo
import fooAudit
import pingAudit
import osAudit
import subdomainAudit


app = FastAPI()

mongo.init()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# foo audit
@app.get("/queue-foo")
async def queue_foo(domain: str):
    new_foo = {
        "type": "foo",
        "domain": domain,
        "completed": False,
        "error": False,
        "result": ""
    }
    saved_foo = mongo.db.foo.insert_one(new_foo)

    # fooAudit.audit_foo(new_foo, saved_foo.inserted_id)
    threading.Thread(target=fooAudit.audit, args=(
        new_foo, saved_foo.inserted_id)).start()

    return {"requestId": str(saved_foo.inserted_id)}


# ping audit
@app.get("/queue-ping")
async def queue_ping(domain: str):
    new_foo = {
        "type": "ping",
        "domain": domain,
        "completed": False,
        "error": False,
        "result": ""
    }
    saved_foo = mongo.db.foo.insert_one(new_foo)

    threading.Thread(target=pingAudit.audit, args=(
        new_foo, saved_foo.inserted_id)).start()

    return {"requestId": str(saved_foo.inserted_id)}


# os audit
@app.get("/queue-os")
async def queue_ping(domain: str):
    new_foo = {
        "type": "os",
        "domain": domain,
        "completed": False,
        "error": False,
        "result": ""
    }
    saved_foo = mongo.db.foo.insert_one(new_foo)

    threading.Thread(target=osAudit.audit, args=(
        new_foo, saved_foo.inserted_id)).start()

    return {"requestId": str(saved_foo.inserted_id)}


# subdomain audit
@app.get("/queue-subdomain")
async def queue_ping(domain: str):
    new_foo = {
        "type": "subdomain",
        "domain": domain,
        "completed": False,
        "error": False,
        "result": ""
    }
    saved_foo = mongo.db.foo.insert_one(new_foo)

    threading.Thread(target=subdomainAudit.audit, args=(
        new_foo, saved_foo.inserted_id)).start()

    return {"requestId": str(saved_foo.inserted_id)}


@app.get("/get-result")
async def get_ping(id: str):
    found_foo = mongo.db.foo.find_one(
        {'_id': ObjectId(id)})
    return {
        "type": found_foo['type'],
        "domain": found_foo['domain'],
        "completed": found_foo['completed'],
        "error": found_foo['error'],
        "result": found_foo['result']
    }
