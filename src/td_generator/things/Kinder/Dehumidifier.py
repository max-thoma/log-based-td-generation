from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "dehumidifier",
            "title": "Dehumidifier",
            "description": "An air dehumidifier with a waste water tank",
            "@type": "Air Dehumidifying Device",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "status": {
                    "title": "Dehumidifier Status",
                    "type": "boolean",
                    "description": "Boolean value representing the status of the device. If True the device is reachable and able to execute actions",
                    "forms": [
                        {
                            "mqv:topic": "dehumidifier/status",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "tank": {
                    "type": "string",
                    "title": "Waster Water Tank Level",
                    "description": "Describes the current state of the waste water tank",
                    "characteristics": ["full", "empty"],
                    "enum": ["full", "empty"],
                    "forms": [
                        {
                            "mqv:topic": "dehumidifier/tank",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "humidity": {
                    "title": "Humidity Level",
                    "type": "integer",
                    "description": "Current humidity level the device aims to reach.",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "mqv:topic": "dehumidifier/humidity",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "toggle status": {
                    "title": "Toggle On/Off",
                    "description": "Toggle status of the device turning it either on or off",
                    "forms": [
                        {
                            "mqv:topic": "dehumidifier/toggle_status",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "dehumidify": {
                    "title": "Start Dehumidification",
                    "description": "Starts the dehumidification process",
                    "forms": [
                        {
                            "mqv:topic": "dehumidifier/dehumidify",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "drain": {
                    "title": "Drain Waste Water Tank",
                    "description": "Drains waste water tank",
                    "forms": [
                        {
                            "mqv:topic": "dehumidifier/drain",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "set humidity": {
                    "title": "Humidity Goal",
                    "description": "Sets the goal humidity",
                    "input": {
                        "type": "integer",
                        "description": "the desired humidity",
                        "minimum": 0,
                        "maximum": 100,
                    },
                    "forms": [
                        {
                            "mqv:topic": "dehumidifier/set_humidity",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
