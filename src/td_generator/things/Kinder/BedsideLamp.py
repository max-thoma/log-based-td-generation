from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "bedside_lamp",
            "title": "Bedside Lamp",
            "description": "A bedside lamp with brightness controls",
            "@type": "Reading Light",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "on": {
                    "type": "boolean",
                    "title": "Lamp Status",
                    "description": "True if Light is turned on",
                    "forms": [
                        {
                            "mqv:topic": "bedside_light/is_on",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "brightness": {
                    "type": "integer",
                    "title": "Lamp Brightness",
                    "description": "Brightness level of the light in percentage",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "mqv:topic": "bedside_light/brightness",
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
                            "mqv:topic": "bedside_light/on",
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
                            "mqv:topic": "bedside_light/off",
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
                            "mqv:topic": "bedside_light/increase",
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
                            "mqv:topic": "bedside_light/decrease",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
