import random

from td import ThingDescription, MESSAGE_NUM


def _mock_state(type=None, min=None, max=None, enum=None, name=None):
    msg = []
    for i in range(0, MESSAGE_NUM):
        msg.append(
            {
                "on": bool(random.randint(0, 1)),
                "bri": random.randint(0, 254),
                "sat": random.randint(0, 254),
            }
        )
    return msg


def td():
    return ThingDescription(
        **{
            "@context": [
                "https://www.w3.org/2019/wot/td/v1",
                {"saref": "https://saref.etsi.org/core/"},
                {"owl": "http://www.w3.org/2002/07/owl#"},
            ],
            "id": "http://192.168.178.41/api/b-eWSAqeP1AUw9hDDC5kidzoRqlwGApvuDGYtVcy/lights/1",
            "title": "Ambient Lightstrip",
            "description": "An ambient light strip with brightness and saturation control",
            "base": "http://192.168.178.41/api/b-eWSAqeP1AUw9hDDC5kidzoRqlwGApvuDGYtVcy/lights/1",
            "@type": "Ambient Light",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "state": {
                    "type": "object",
                    "title": "Ambient Light State",
                    "description": "State of the Ambient Lightstrip, this includes on/off status, brightness and saturation",
                    "forms": [
                        {
                            "mqv:topic": "state",
                            "mediaType": "application/Json",
                            "op": ["readproperty", "writeproperty"],
                            "htv:methodName": "GET",
                            "mock": _mock_state,
                        }
                    ],
                    "properties": {
                        "on": {
                            "type": "boolean",
                            "description": "Boolean Value that describes if the device is on or off",
                        },
                        "bri": {
                            "title": "Brightness",
                            "description": "Value between 0 and 254 indicating the Brightness of the Light",
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 254,
                        },
                        "sat": {
                            "title": "Saturation",
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 254,
                            "descriptions": "Sets the intensity of the colors. Value between 0 and 254, with 254 indicating maximum saturation",
                        },
                    },
                }
            },
            "actions": {
                "turn on": {
                    "title": "Turn On Ambient Light Strip",
                    "description": "Turns the Light on",
                    "forms": [
                        {
                            "mqv:topic": "turn_on",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "turn off": {
                    "title": "Turn Off Ambient Light Strip",
                    "description": "Turns the Light off",
                    "forms": [
                        {
                            "mqv:topic": "turn_off",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "set brightness": {
                    "title": "Set Brightness",
                    "description": "Sets the brightness",
                    "forms": [
                        {
                            "mqv:topic": "set_brightness",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "PUT",
                        }
                    ],
                    "input": {"type": "integer"},
                },
                "set saturation": {
                    "title": "Set Saturation",
                    "description": "Sets the saturation",
                    "forms": [
                        {
                            "mqv:topic": "set_saturation",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "PUT",
                        }
                    ],
                    "input": {"type": "integer"},
                },
            },
        }
    )
