from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Push Button",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "PushButton",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A push button",
            "mqv:topic": "things/id-15",
            "properties": {
                "pushed": {
                    "name": "pushed",
                    "value": False,
                    "title": "Pushed",
                    "description": "A 'true' value indicates that the button is currently pressed. Otherwise, the value defaults to 'false'",
                    "type": "boolean",
                    "@type": "PushedProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-15/properties/pushed"},
                        {
                            "mqv:topic": "things/id-15/properties/pushed",
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
                    "mqv:topic": "things/id-15",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-15",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-15/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-15/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 14,
            "selectedCapability": "PushButton",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-15",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-15:readwrite",
                        "/things/id-15",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
