from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "CeilingFan",
            "title": "Bedroom Ceiling Fan",
            "id": "urn:uuid:94daccad-98e6-43f5-b757-3ab122650b81",
            "description": "A ceiling fan with different modes",
            "properties": {
                "state": {
                    "title": "Fan State",
                    "description": "State of the fan",
                    "observable": True,
                    "type": "string",
                    "enum": ["UNKNOWN", "ON", "OFF"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "bedroom_fan/ceil/status",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "oscillationState": {
                    "title": "Oscillation State",
                    "description": "Indicates if the fan is oscillating or not",
                    "observable": True,
                    "type": "boolean",
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "bedroom_fan/ceil/oscillation",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
            "events": {
                "staling": {
                    "title": "Fan Staling",
                    "description": "This event is triggered when the fan has stalled",
                    "data": {"type": "string", "enum": ["STALED", "OPERATIONAL"]},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "bedroom_fan/ceil/staling",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                }
            },
            "actions": {
                "setMode": {
                    "title": "Fan Mode",
                    "description": "Set the fan mode: auto, smart, woosh, eco, night or breeze",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": ["auto", "smart", "woosh", "eco", "night", "breeze"],
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "response": {"contentType": "text/plain"},
                            "mqv:topic": "bedroom_fan/ceil/set/mode",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "setSpeed": {
                    "title": "Fan speed",
                    "description": "Set the fan speed in percent",
                    "input": {
                        "observable": True,
                        "type": "number",
                        "minimum": 0,
                        "maximum": 100,
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "response": {"contentType": "text/plain"},
                            "mqv:topic": "bedroom_fan/ceil/set/speed",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
