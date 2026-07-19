import json

def serialize(record):

    return json.dumps(record).encode("utf-8")