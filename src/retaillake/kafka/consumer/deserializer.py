import json


def deserialize(value: bytes):

    return json.loads(value.decode("utf-8"))