from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Motion Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "MotionSensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that can detect and report motion",
            "mqv:topic": "things/id-14",
            "properties": {
                "motion": {
                    "name": "motion",
                    "value": False,
                    "title": "Motion",
                    "description": "This property is 'true' when motion was detected and 'false', if no motion was detected",
                    "type": "boolean",
                    "@type": "MotionProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-14/properties/motion"},
                        {
                            "mqv:topic": "things/id-14/properties/motion",
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
                    "mqv:topic": "things/id-14",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-14",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-14/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-14/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 13,
            "selectedCapability": "MotionSensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-14",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-14:readwrite",
                        "/things/id-14",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
