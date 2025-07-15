from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Smoke Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "SmokeSensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that can detect smoke",
            "mqv:topic": "things/id-30",
            "properties": {
                "smoke": {
                    "name": "smoke",
                    "value": False,
                    "title": "Smoke",
                    "description": "Indicated whether smoke was detected",
                    "type": "boolean",
                    "@type": "SmokeProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-30/properties/smoke"},
                        {
                            "mqv:topic": "things/id-30/properties/smoke",
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
                    "mqv:topic": "things/id-30",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-30",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-30/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-30/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 28,
            "selectedCapability": "SmokeSensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-30",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-30:readwrite",
                        "/things/id-30",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
