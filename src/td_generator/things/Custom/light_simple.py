from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "LightBulb",
            "title": "Dimmable Light Bulb",
            "id": "urn:uuid:e9303dd9-2565-4468-b0e0-106c408959a9",
            "description": "A dimmable light bulb",
            "actions": {
                "setBrightness": {
                    "title": "Brightness",
                    "description": "Set the brightness of the light bulb",
                    "input": {
                        "observable": True,
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 255,
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "mqv:topic": "application/my_bulb/set",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                }
            },
        }
    )
