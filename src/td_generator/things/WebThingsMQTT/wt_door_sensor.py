from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Door Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "DoorSensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that observes the state of a door",
            "mqv:topic": "things/id-13",
            "properties": {
                "open": {
                    "name": "open",
                    "value": False,
                    "title": "Open",
                    "description": "The current open/close state of the door indicated by boolean value",
                    "type": "boolean",
                    "@type": "OpenProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-13/properties/open"},
                        {
                            "mqv:topic": "things/id-13/properties/open",
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
                    "mqv:topic": "things/id-13",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-13",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-13/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-13/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 12,
            "selectedCapability": "DoorSensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-13",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-13:readwrite",
                        "/things/id-13",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
