from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Multi-level Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "MultiLevelSensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that can measure a level",
            "mqv:topic": "things/id-5",
            "properties": {
                "on": {
                    "name": "on",
                    "value": False,
                    "title": "On/Off",
                    "description": "Indicates whether the sensor is on or off",
                    "type": "boolean",
                    "@type": "BooleanProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-5/properties/on"},
                        {
                            "mqv:topic": "things/id-5/properties/on",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "level": {
                    "name": "level",
                    "value": 0,
                    "title": "Level",
                    "description": "A level reading from 0 to 100",
                    "type": "number",
                    "@type": "LevelProperty",
                    "unit": "percent",
                    "minimum": 0,
                    "maximum": 100,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-5/properties/level"},
                        {
                            "mqv:topic": "things/id-5/properties/level",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
            },
            "actions": {},
            "events": {},
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "mqv:topic": "things/id-5",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-5",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-5/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-5/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 6,
            "selectedCapability": "MultiLevelSensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-5",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-5:readwrite",
                        "/things/id-5",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
