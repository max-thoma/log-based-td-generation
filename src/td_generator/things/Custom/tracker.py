import random

from td import ThingDescription
from td import MESSAGE_NUM


def _mock_location(type=None, min=None, max=None, enum=None, name=None):
    msg = []
    for i in range(0, MESSAGE_NUM):
        msg.append(
            {
                "longitude": round(random.uniform(0, 45), 3),
                "latitude": round(random.uniform(0, 45), 3),
                "altitude": round(random.uniform(0, 10), 3),
            }
        )
    return msg


def _mock_set(type=None, min=None, max=None, enum=None, name=None):
    msg = []
    for i in range(0, MESSAGE_NUM):
        msg.append(
            {
                "longitude": round(random.uniform(0, 45), 3),
                "latitude": round(random.uniform(0, 45), 3),
                "radius": round(random.uniform(0, 50), 3),
            }
        )
    return msg


# https://www.w3.org/TR/wot-thing-description11/#saref-geolocation-annotation-example-2
def td():
    return ThingDescription(
        **{
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
            ],
            "@type": "Tracker",
            "title": "My Smart Position Tracker",
            "id": "urn:uuid:8ca4d0a0-b788-4d9d-af99-7a032a732f13",
            "description": "A GPS location tracker",
            "properties": {
                "position": {
                    "title": "Tracker Position",
                    "description": "The location of the tracker in GPS coordinates",
                    "observable": True,
                    "type": "object",
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "homeassistant/device_tracker/a4567d663eaf/pos",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                            "mock": _mock_location,
                        }
                    ],
                    "properties": {
                        "longitude": {"type": "number"},
                        "latitude": {"type": "number"},
                        "altitude": {"type": "number"},
                    },
                }
            },
            "events": {
                "alarm": {
                    "title": "Movement Alarm",
                    "description": "The tracker has left the set position and radius",
                    "data": {"type": "null"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "homeassistant/device_tracker/a4567d663eaf/alarm",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                }
            },
            "actions": {
                "setPosition": {
                    "title": "Set Position",
                    "description": "Set the position and radius of the tracker",
                    "input": {
                        "observable": True,
                        "type": "object",
                        "properties": {
                            "longitude": {"type": "number"},
                            "latitude": {"type": "number"},
                            "radius": {"type": "number"},
                        },
                    },
                    "output": {"observable": False, "type": "null"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "homeassistant/device_tracker/a4567d663eaf/config",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                            "mock": _mock_set,
                        }
                    ],
                }
            },
        }
    )
