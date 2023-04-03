from pymongo import MongoClient


def mongodb_audit(domain):
    try:
        mc = MongoClient(f'mongodb://{domain}:27017/')
        target_db = mc['test']
        target_db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
                                      {"x": 2, "tags": ["cat"]},
                                      {"x": 2, "tags": [
                                          "mouse", "cat", "dog"]},
                                      {"x": 3, "tags": []}])
        return "Unsecured mongodb found on port 27017"
    except Exception as e:
        print(e)
        return "No unsecured mongodb found"


if __name__ == '__main__':
    print(mongodb_audit('google.com'))
