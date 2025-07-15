from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "oven",
            "title": "kettle",
            "description": "A smart kettle that can be filled, emptied and activated remotely.",
            "@type": "Kettle",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "power": {
                    "type": "boolean",
                    "title": "Kettle On/Off Status",
                    "description": "Indicates if the kettle is currently turned on and ready for the heating process or in standby",
                    "characteristics": ["on", "off"],
                    "forms": [
                        {
                            "mqv:topic": "kettle/power",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "filled": {
                    "type": "boolean",
                    "title": "Kettle Filled",
                    "description": "Indicates whether the kettle is filled with water or not",
                    "forms": [
                        {
                            "mqv:topic": "kettle/is_filled",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "switch power": {
                    "title": "Turn On/Off",
                    "description": "Turns the kettle on or off depending on the current state",
                    "forms": [
                        {
                            "mqv:topic": "kettle/switch_power",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "heat": {
                    "title": "Start Boiling",
                    "description": "Start the heating process of the kettle",
                    "forms": [
                        {
                            "mqv:topic": "kettle/heat",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "fill": {
                    "title": "Fill Kettle",
                    "description": "Fills the kettle with water",
                    "forms": [
                        {
                            "mqv:topic": "kettle/fill",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "empty": {
                    "title": "Empty Kettle",
                    "description": "Empties the kettle with water",
                    "forms": [
                        {
                            "mqv:topic": "kettle/empty",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
