import datetime
import time

from td import ThingDescription
from td import MESSAGE_NUM


def _mock(type=None, min=None, max=None, enum=None, name=None):
    msg = []
    now = datetime.datetime.now()
    step = datetime.timedelta(minutes=5)
    for i in range(0, MESSAGE_NUM):
        t = now + i * step
        msg.append(int(time.mktime(t.timetuple())))
    return msg


def td():
    return ThingDescription(
        **{
            "@type": "Doorbell",
            "title": "My Frontdoor Doorbell",
            "id": "urn:uuid:bc4c5201-1540-4229-871f-37c9ea7058a1",
            "description": "The front doorbell",
            "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
            "security": ["nosec_sc"],
            "properties": {
                "availability": {
                    "title": "Availability",
                    "description": "Availability status of the doorbell",
                    "observable": True,
                    "type": "string",
                    "enum": ["ONLINE", "OFFLINE"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "home/front/db/avail",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                }
            },
            "events": {
                "ring": {
                    "title": "Doorbell Ring",
                    "description": "This event is triggered when the doorbell is rung",
                    "data": {
                        "title": "Timestamp",
                        "description": "POSIX timestamp when the bell was rung",
                        "type": "integer",
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "response": {"contentType": "text/plain"},
                            "mqv:topic": "home/front/db/ring",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                            "mock": _mock,
                        }
                    ],
                }
            },
        }
    )
