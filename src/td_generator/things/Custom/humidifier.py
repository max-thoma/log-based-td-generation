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
            "@type": "AirHumidifier",
            "title": "Air Humidifier",
            "id": "urn:uuid:5676e5b0-9e2d-473c-879f-1e226ce3192c",
            "description": "An air humidifier with multiple modes",
            "properties": {
                "state": {
                    "title": "Fan State",
                    "description": "Current state of the humidifier",
                    "observable": True,
                    "type": "string",
                    "enum": ["UNKNOWN", "ON", "OFF", "IDLE"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "living_room/humidifier/status",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "humidity": {
                    "title": "Air Humidity",
                    "description": "Current air humidity in percent",
                    "observable": True,
                    "type": "integer",
                    "minimum": 5,
                    "maximum": 95,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "living_room/humidifier/humidity",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
            "events": {
                "targetReached": {
                    "title": "Target Reached",
                    "description": "The humidity target has been reached",
                    "data": {
                        "title": "Timestamp",
                        "description": "POSIX timestamp when the target was reached",
                        "type": "integer",
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "living_room/humidifier/target/ok",
                            "mqv:retain": True,
                            "op": ["subscribeevent", "unsubscribeevent"],
                            "mock": _mock,
                        }
                    ],
                },
                "belowThreshold": {
                    "title": "Below Threshold",
                    "description": "The humidity is below the threshold",
                    "data": {
                        "title": "Timestamp",
                        "description": "POSIX timestamp when the humidity was below the set threshold",
                        "type": "integer",
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "living_room/humidifier/threshold/below",
                            "mqv:retain": True,
                            "op": ["subscribeevent", "unsubscribeevent"],
                            "mock": _mock,
                        }
                    ],
                },
            },
            "actions": {
                "setTarget": {
                    "title": "Target Humidity",
                    "description": "Set the humidity target",
                    "input": {
                        "observable": True,
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 100,
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "response": {"contentType": "text/plain"},
                            "mqv:topic": "living_room/humidifier/target/set",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "setThreshold": {
                    "title": "Threshold Humidity",
                    "description": "Set the humidity threshold target in percent",
                    "input": {
                        "observable": True,
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 100,
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "response": {"contentType": "text/plain"},
                            "mqv:topic": "living_room/humidifier/threshold/set",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "setMode": {
                    "title": "Humidifier Mode",
                    "description": "Set the mode of the humidifier",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": [
                            "normal",
                            "eco",
                            "away",
                            "boost",
                            "comfort",
                            "home",
                            "sleep",
                            "auto",
                            "baby",
                        ],
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "living_room/humidifier/set/mode",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "setState": {
                    "title": "Humidifier On/Off-State",
                    "description": "Turn the humidifier on or off",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": ["on", "off"],
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "living_room/humidifier/set/state",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
