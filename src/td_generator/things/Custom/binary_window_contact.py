from td import ThingDescription

def td():

    return ThingDescription(
        **{
            "@type": "WindowContact",
            "title": "Binary Window Contact",
            "id": "urn:uuid:24abed48-e9e3-4839-b1a4-f189f763ec89",
            "description": "A sensor that monitors the state of a window",
            "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
            "security": ["nosec_sc"],
            "properties": {
                "state": {
                    "title": "Window Sensor State",
                    "description": "The state of the window",
                    "observable": True,
                    "type": "string",
                    "enum": ["open", "closed", "unknown"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "home-assistant/window/contact",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
                "availability": {
                    "title": "Sensor Availability",
                    "description": "Availability status of the window sensor",
                    "observable": True,
                    "type": "string",
                    "enum": ["unavailable", "available"],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "home-assistant/window/availability",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                },
            },
        }
    )
