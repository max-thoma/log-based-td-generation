from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "On/Off Switch",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "OnOffSwitch",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A switch that remotely turns on or of a device",
            "mqv:topic": "things/id-3",
            "properties": {
                "on": {
                    "name": "on",
                    "value": False,
                    "title": "On/Off",
                    "description": "Indicates the current state of the switch",
                    "type": "boolean",
                    "@type": "OnOffProperty",
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-3/properties/on"},
                        {
                            "mqv:topic": "things/id-3/properties/on",
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
                    "mqv:topic": "things/id-3",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-3",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-3/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-3/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 4,
            "selectedCapability": "OnOffSwitch",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-3",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-3:readwrite",
                        "/things/id-3",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
