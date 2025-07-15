from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "VacuumCleaner",
            "title": "Vacuum Cleaner",
            "id": "urn:uuid:b5d392d8-9931-44be-881e-d12410860baa",
            "description": "A smart vacuum cleaner",
            "properties": {
                "state": {
                    "title": "Vacuum Cleaner State",
                    "description": "The state of the vacuum. The state may be cleaning, docked, paused, idle, returning or error",
                    "observable": True,
                    "type": "string",
                    "enum": [
                        "cleaning",
                        "docked",
                        "paused",
                        "idle",
                        "returning",
                        "error",
                    ],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "apartment/vacuum/state",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "battery": {
                    "title": "Battery",
                    "description": "Battery percentage of the vacuum cleaner",
                    "observable": True,
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "apartment/vacuum/bat",
                            "mqv:retain": True,
                            "op": ["observeproperty"],
                        }
                    ],
                },
            },
            "bin": {
                "title": "Bin",
                "description": "State of the bin, it may be empty, medium or full. If bin is full, it needs emptying.",
                "observable": True,
                "type": "string",
                "enum": ["empty", "medium", "full"],
                "forms": [
                    {
                        "href": "192.168.0.100:1883",
                        "mqv:topic": "apartment/vacuum/bin/state",
                        "mqv:retain": True,
                        "op": ["observeproperty"],
                    }
                ],
            },
            "events": {
                "stuck": {
                    "title": "Vacuum Stuck",
                    "description": "The vacuum cleaner is stuck and needs assistance",
                    "data": {"type": "null"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "apartment/vacuum/stuck",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
                "bin": {
                    "title": "Vacuum Bin Full",
                    "description": "The vacuum cleaner's bin is full",
                    "data": {"type": "null"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "apartment/vacuum/bin/full",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
            },
            "actions": {
                "command": {
                    "title": "Commands",
                    "description": "Send commands to the vacuum cleaner",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": [
                            "start",
                            "pause",
                            "return",
                            "stop",
                            "clean_spot",
                            "locate",
                        ],
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "apartment/vacuum/cmnd",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "pause": {
                    "title": "Pause vacuum cleaner",
                    "description": "Pause the vacuum cleaner",
                    "input": {
                        "observable": True,
                        "type": "boolean",
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "apartment/vacuum/pause",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
