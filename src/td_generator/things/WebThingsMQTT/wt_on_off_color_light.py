from td import ThingDescription

def _mock_color(type=None, min=None, max=None, enum=None, name=None):
    return [
        "#5287a4",
        "#a45d50",
        "#9aa712",
        "#0abbf2",
        "#86b8ce",
    ]  # random colors


def td():
    return ThingDescription(
        **{
            "title": "On/Off Color Light",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "LightControlSwitch",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A light that can be color controlled",
            "mqv:topic": "things/id-0",
            "properties": {
                "on": {
                    "name": "on",
                    "value": False,
                    "title": "On/Off",
                    "description": "Indicates whether the light is switched on or off",
                    "type": "boolean",
                    "@type": "OnOffProperty",
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-0/properties/on"},
                        {
                            "mqv:topic": "things/id-0/properties/on",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "color": {
                    "name": "color",
                    "value": "#ffffff",
                    "title": "Color",
                    "description": "The current light color as hexadecimal color code",
                    "type": "string",
                    "@type": "ColorProperty",
                    "readOnly": False,
                    "links": [],
                    "forms": [
                        {
                            "mqv:topic": "things/id-0/properties/color",
                            "mock": _mock_color,
                        },
                        {
                            "mqv:topic": "things/id-0/properties/color",
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
                    "mqv:topic": "things/id-0",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-0",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-0/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-0/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 1,
            "selectedCapability": "Light",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-0",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-0:readwrite",
                        "/things/id-0",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
