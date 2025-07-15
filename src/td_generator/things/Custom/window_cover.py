from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "WindowCover",
            "title": "My Smart Window Cover",
            "id": "urn:uuid:8504295f-d7e3-4c34-9c1d-d380816a6022",
            "description": "An automatic window cover",
            "properties": {
                "position": {
                    "title": "Cover position",
                    "description": "Position of the cover, it is either open or closed",
                    "observable": True,
                    "type": "string",
                    "enum": ["OPEN", "CLOSED"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "home/cover/pos",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                }
            },
            "events": {
                "positionChange": {
                    "title": "Position Change",
                    "description": "The position of the window cover has changed",
                    "data": {
                        "type": "string",
                        "enum": ["OPENING", "CLOSING"],
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "home/cover/chg",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
                "sunLight": {
                    "title": "Sun light detection",
                    "description": "The window cover has detected sunlight",
                    "data": {
                        "type": "string",
                        "enum": ["LOW", "MEDIUM", "HIGH"],
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "home/cover/light",
                            "mqv:retain": True,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                },
            },
            "actions": {
                "command": {
                    "title": "Cover Commands",
                    "description": "Change the cover position to open or closed",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": ["OPEN", "CLOSE"],
                    },
                    "output": {
                        "observable": False,
                        "type": "null",
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "home/cover/cmd",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                }
            },
        }
    )
