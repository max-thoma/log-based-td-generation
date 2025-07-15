from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Binary Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "BinarySensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A binary sensor, that can be in either of two states: 'on' or 'off'",
            "mqv:topic": "things/id-4",
            "properties": {
                "on": {
                    "name": "on",
                    "value": False,
                    "title": "On/Off",
                    "description": "The sensor can be either on, indicated by a 'true', or off, indicated by a 'false'",
                    "type": "boolean",
                    "@type": "BooleanProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-4/properties/on"},
                        {
                            "mqv:topic": "things/id-4/properties/on",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                }
            },
            "actions": {},
            "events": {},
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "mqv:topic": "things/id-4",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-4",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-4/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-4/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 5,
            "selectedCapability": "BinarySensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-4",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-4:readwrite",
                        "/things/id-4",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
