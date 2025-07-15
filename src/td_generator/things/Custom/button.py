from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "SmartButton",
            "title": "Smart Push Button",
            "id": "urn:uuid:6f06a2fb-706e-41b4-9245-917c38c5c61f",
            "description": "A smart push button that can be used to automate stuff",
            "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
            "security": ["nosec_sc"],
            "properties": {
                "availability": {
                    "title": "Button Availability",
                    "description": "Availability status of the button",
                    "observable": True,
                    "type": "string",
                    "enum": ["unavailable", "available"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "home/bedroom/switch1/availability",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                }
            },
            "events": {
                "pressed": {
                    "title": "Button Press",
                    "description": "This is the event that occurs when the button is pressed",
                    "data": {"type": "null"},
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "response": {"contentType": "text/plain"},
                            "mqv:topic": "home/bedroom/switch1/pressed",
                            "mqv:retain": False,
                            "op": ["subscribeevent", "unsubscribeevent"],
                        }
                    ],
                }
            },
        }
    )
