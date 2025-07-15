from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "LawnMower",
            "title": "Lawn Mower",
            "id": "urn:uuid:ad29cf9d-e767-4c45-aff7-7919beb5bedb",
            "description": "A smart lawn mower",
            "properties": {
                "activity": {
                    "title": "Mower State",
                    "description": "The state of the lawn mower, it can be docked, undocked, charging or mowing the lawn.",
                    "observable": True,
                    "type": "string",
                    "enum": ["UNDOCKED", "DOCKED", "CHARGING", "MOWING"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "lawn_mower_plus/state",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "battery": {
                    "title": "Battery",
                    "description": "Battery percentage of the lawn mower",
                    "observable": True,
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "lawn_mower_plus/soc",
                            "mqv:retain": True,
                            "op": ["observeproperty"],
                        }
                    ],
                },
                "reachEstimate": {
                    "title": "Reach Estimate",
                    "description": "Estimated reach in minutes until next recharge",
                    "observable": True,
                    "type": "integer",
                    "minimum": 0,
                    "maximum": 250,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "lawn_mower_plus/reach",
                            "mqv:retain": True,
                            "op": ["observeproperty"],
                        }
                    ],
                },
            },
            "events": {
                "dock": {
                    "title": "Docking State Changed",
                    "description": "The docking state has changed",
                    "data": {"type": "string", "enum": ["DOCKED", "UNDOCKED"]},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "lawn_mower_plus/dock/status",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
            },
            "actions": {
                "start": {
                    "title": "Start Job",
                    "description": "Initiate a new lawn mower job",
                    "input": {
                        "observable": True,
                        "type": "boolean",
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "lawn_mower_plus/start",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "pause": {
                    "title": "Pause Job",
                    "description": "Pause the lawn mower job",
                    "input": {
                        "observable": True,
                        "type": "boolean",
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "lawn_mower_plus/pause",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
                "docked": {
                    "title": "Dock lawn mower",
                    "description": "Dock the lawn mower",
                    "input": {
                        "observable": True,
                        "type": "boolean",
                    },
                    "output": None,
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "lawn_mower_plus/dock",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                },
            },
        }
    )
