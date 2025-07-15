from matplotlib.pyplot import title

from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "exterior_light",
            "title": "Exterior Light",
            "description": "An exterior light with brightness control",
            "@type": "Exterior Light",
            "base": "http://127.0.0.1:5000",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "status": {
                    "type": "boolean",
                    "title": "Exterior Light On/Off",
                    "description": "True if Light is turned on",
                    "forms": [
                        {
                            "mqv:topic": "exterior_light/is_on",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "brightness": {
                    "type": "integer",
                    "title": "Brightness Level",
                    "description": "Brightness level of the light in percentage",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "mqv:topic": "exterior_light/brightness",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "turn on": {
                    "title": "Turn On",
                    "description": "Turns the light on",
                    "forms": [
                        {
                            "mqv:topic": "exterior_light/on",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "turn off": {
                    "title": "Turn Off",
                    "description": "Turns the light off",
                    "forms": [
                        {
                            "mqv:topic": "exterior_light/off",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "increase": {
                    "title": "Increase Brightness",
                    "description": "Increases brightness by 10%",
                    "forms": [
                        {
                            "mqv:topic": "exterior_light/increase",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "decrease": {
                    "title": "Decrease Brightness",
                    "description": "Decreases brightness by 10%",
                    "forms": [
                        {
                            "mqv:topic": "exterior_light/decrease",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
