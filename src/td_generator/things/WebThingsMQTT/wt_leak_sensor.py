from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Leak Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "LeakSensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that can detect a water leak",
            "mqv:topic": "things/id-16",
            "properties": {
                "leak": {
                    "name": "leak",
                    "value": False,
                    "title": "Leak",
                    "description": "This property indicates whether a leak has been detected",
                    "type": "boolean",
                    "@type": "LeakProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-16/properties/leak"},
                        {
                            "mqv:topic": "things/id-16/properties/leak",
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
                    "mqv:topic": "things/id-16",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-16",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-16/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-16/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 15,
            "selectedCapability": "LeakSensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-16",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-16:readwrite",
                        "/things/id-16",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
