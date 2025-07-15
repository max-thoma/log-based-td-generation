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
            "@type": "PhotovoltaicInverter",
            "title": "PV Inverter",
            "id": "urn:uuid:1198aaed-ac5a-4fc7-b2bc-340f1b24bc66",
            "description": "A Photovoltaic Inverter",
            "properties": {
                "inverterStatus": {
                    "title": "Invert Status",
                    "description": "Status of the PV inverter. There are 13 different states",
                    "observable": True,
                    "type": "string",
                    "enum": [
                        "00-On sector",
                        "01-Power failure / On battery",
                        "02-Loss of communication",
                        "03-Battery fault",
                        "04-System shutdown",
                        "05-Tension dip",
                        "06-Overvoltage",
                        "07-Voltage drop",
                        "08-Voltage increase",
                        "09-Line noise",
                        "10-Frequency variation",
                        "11-Transient distortion",
                        "12-Harmonic distortion",
                    ],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "cellar/inverter/status",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "current": {
                    "title": "Current",
                    "description": "Current draw of the L1, L2 and L3 phases",
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
                            "mqv:topic": "cellar/inverter/current",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                            "mock": _mock,
                        }
                    ],
                },
                "activePower": {
                    "title": "Active Power",
                    "description": "Active Power running through the inverter",
                    "observable": True,
                    "type": "number",
                    "minimum": 0,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "cellar/inverter/active_power",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "reactivePower": {
                    "title": "Reactive Power",
                    "description": "Reactive Power measured by the inverter",
                    "observable": True,
                    "type": "number",
                    "minimum": 0,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "cellar/inverter/reactive_power",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "temperature": {
                    "title": "Temperature PV Inverter",
                    "description": "Internal temperature of PV inverter",
                    "observable": True,
                    "type": "number",
                    "minimum": 0,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "cellar/inverter/temperature",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
            "events": {
                "enabled": {
                    "title": "Inverter Enabled",
                    "description": "The inverter was enabled/disabled",
                    "data": {"type": "boolean"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "cellar/inverter/current_state",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
                "error": {
                    "title": "Error Event",
                    "description": "An error has been encountered at the inverter",
                    "data": {"type": "null"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "cellar/inverter/error",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
            },
            "actions": {
                "turnOn": {
                    "title": "Enable Inverter",
                    "description": "Turn on the Inverter",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": ["ON", "OFF", "0", "1"],
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "cellar/inverter/cmnd",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
