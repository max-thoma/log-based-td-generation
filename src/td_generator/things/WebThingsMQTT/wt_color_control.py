from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Color Control",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "ColorControl",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A device that can control colors",
            "mqv:topic": "things/id-23",
            "properties": {
                "color": {
                    "name": "color",
                    "title": "Color",
                    "description": "The currently selected color",
                    "type": "string",
                    "enum": [
                        "Red",
                        "LimeGreen",
                        "Yellow",
                        "DarkGreen",
                        "LightCyan",
                    ],  # random colors
                    "@type": "ColorProperty",
                    "readOnly": False,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-23/properties/color"},
                        {
                            "mqv:topic": "things/id-23/properties/color",
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
                    "mqv:topic": "things/id-23",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-23",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-23/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-23/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 21,
            "selectedCapability": "ColorControl",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-23",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-23:readwrite",
                        "/things/id-23",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
