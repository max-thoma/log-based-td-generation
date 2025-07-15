import random

from td import ThingDescription, MESSAGE_NUM


def _mock(type=None, min=None, max=None, enum=None, name=None):
    msg = []
    for i in range(0, MESSAGE_NUM):
        msg.append(
            {
                "r": random.randint(0, 256),
                "g": random.randint(0, 256),
                "b": random.randint(0, 256),
            }
        )
    return msg


def td():
    return ThingDescription(
        **{
            "@type": "RGBLightBulb",
            "title": "RGB Light Bulb",
            "id": "urn:uuid:3e5c2737-e72a-44f0-a238-6681e2f3ae95",
            "description": "A dimmable RGB light bulb",
            "properties": {
                "status": {
                    "title": "Bulb State",
                    "description": "The current state of the light bulb, it can be on, off or failed",
                    "type": "string",
                    "enum": ["On", "Off", "Failed"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "application/bulb/status",
                            "mqv:retain": True,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                }
            },
            "actions": {
                "set": {
                    "title": "Brightness RGB channels",
                    "description": "Set the brightness of the individual R, G and B channel",
                    "input": {
                        "observable": True,
                        "type": "object",
                        "properties": {
                            "r": {
                                "description": "Red channel",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 255,
                            },
                            "g": {
                                "description": "Green channel",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 255,
                            },
                            "b": {
                                "description": "Blue channel",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 255,
                            },
                        },
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "application/bulb/set",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                            "mock": _mock,
                        }
                    ],
                },
                "power": {
                    "title": "Power",
                    "description": "Turn the bulb on or off",
                    "input": {
                        "observable": True,
                        "type": "boolean",
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "application/bulb/power",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
