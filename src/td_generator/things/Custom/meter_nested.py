from td import ThingDescription, MESSAGE_NUM
import random


def _mock_current(type=None, min=None, max=None, enum=None, name=None):
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


def _mock_power(type=None, min=None, max=None, enum=None, name=None):
    msg = []
    for i in range(0, MESSAGE_NUM):
        msg.append(
            {
                "Total": round(random.uniform(0, 3000), 3),
                "Today": round(random.uniform(0, 300), 3),
                "Now": round(random.uniform(0, 3), 3),
            }
        )
    return msg


def td():
    return ThingDescription(
        **{
            "@type": "SmartMeter",
            "title": "Smart Meter",
            "id": "urn:uuid:de06e393-c7ed-473e-ae20-6a38a4798680",
            "description": "A Smart Meter",
            "properties": {
                "status": {
                    "title": "Status",
                    "description": "Status of the SM",
                    "observable": True,
                    "type": "string",
                    "enum": ["OK", "ERROR"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "smart_meter/status",
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
                            "mqv:topic": "smart_meter/current",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                            "mock": _mock_current,
                        }
                    ],
                },
                "power": {
                    "title": "Power",
                    "description": "Current power consumption as measured by the SM",
                    "observable": True,
                    "type": "object",
                    "properties": {
                        "total": {
                            "title": "Total Energy",
                            "description": "The total energy consumption measured by the SM",
                            "type": "number",
                        },
                        "today": {
                            "title": "Total Energy",
                            "description": "The total daily energy consumption measured by the SM",
                            "observable": True,
                            "type": "number",
                        },
                        "now": {
                            "title": "Total Energy",
                            "description": "The energy consumption measured by the SM in the last 15 min",
                            "observable": True,
                            "type": "number",
                        },
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "smart_meter/power",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                            "mock": _mock_power,
                        }
                    ],
                },
            },
        }
    )
