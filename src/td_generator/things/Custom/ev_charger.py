import random

from td import ThingDescription
from td import MESSAGE_NUM


def _mock(type=None, min=None, max=None, enum=None, name=None):
    msg = []
    for i in range(0, MESSAGE_NUM):
        msg.append(
            {
                "L1": round(random.uniform(0, 16), 3),
                "L2": round(random.uniform(0, 16), 3),
                "L3": round(random.uniform(0, 16), 3),
            }
        )
    return msg


def td():
    return ThingDescription(
        **{
            "@type": "EvCharger",
            "title": "EV Charger",
            "id": "urn:uuid:bacf4c15-8bae-4a33-b067-4c88b802f7c7",
            "description": "An EV charger",
            "properties": {
                "chargerStatus": {
                    "title": "Status Code",
                    "description": "Status of the charger compliant wiht SAE_J1772",
                    "observable": True,
                    "type": "string",
                    "enum": ["A", "B", "C", "D", "E", "F"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charger/status",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "current": {
                    "title": "Current",
                    "description": "Current of the L1, L2 and L3 phases",
                    "observable": True,
                    "type": "object",
                    "properties": {
                        "L1": {"type": "number", "description": "Current of L1"},
                        "L2": {"type": "number", "description": "Current of L2"},
                        "L3": {"type": "number", "description": "Current of L3"},
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charger/current",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                            "mock": _mock,
                        }
                    ],
                },
                "power": {
                    "title": "Power",
                    "description": "Current power consumption of charger",
                    "observable": True,
                    "type": "number",
                    "minimum": -3600,
                    "maximum": 3600,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charger/power",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
            "events": {
                "enabled": {
                    "title": "Charger Enabled",
                    "description": "Indicates whether the charger is enabled or disabled",
                    "data": {"type": "boolean"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/ev/charger/enabled",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                }
            },
            "actions": {
                "enable": {
                    "title": "Enable Charger",
                    "description": "Enable/disable EV charger",
                    "input": {"observable": True, "type": "boolean"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/charger/enable",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "maxCurrent": {
                    "title": "Max Current Charger",
                    "description": "Set the max. current of EV charger in Ampere",
                    "minimum": 0,
                    "maximum": 32,
                    "input": {"observable": True, "type": "integer"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "garage/charger/maxCurrent",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
