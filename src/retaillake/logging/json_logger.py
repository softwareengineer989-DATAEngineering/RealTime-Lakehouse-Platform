"""
Reserved for structured JSON logging.

Future sprint:
- ELK
- Splunk
- OpenSearch
- CloudWatch
"""

"""
Reserved for structured JSON logging.

Sprint 13 will extend this module to emit
JSON formatted logs suitable for ELK,
Datadog, Splunk and cloud logging systems.
"""

import json


def to_json(record: dict) -> str:
    """
    Convert dictionary log record into JSON.
    """

    return json.dumps(record)
