from td import ThingDescription
from td import MESSAGE_NUM


def _mock_color(type=None, min=None, max=None, enum=None, name=None):
    return [
        "#ba329d",
        "#8f3fcc",
        "#1c63d2",
        "#13ac91",
        "#7a9d12",
    ]


def td():
    return ThingDescription(
        **{
            "title": "Color Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "ColorSensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that can measure colors",
            "mqv:topic": "things/id-26",
            "properties": {
                "color": {
                    "name": "color",
                    "value": "#ffffff",
                    "title": "Color",
                    "description": "The hex code of the measured color",
                    "type": "string",
                    "@type": "ColorProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {
                            "mqv:topic": "things/id-26/properties/color",
                            "mock": _mock_color,
                        },
                        {
                            "mqv:topic": "things/id-26/properties/color",
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
                    "mqv:topic": "things/id-26",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-26",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-26/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-26/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 24,
            "selectedCapability": "ColorSensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-26",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-26:readwrite",
                        "/things/id-26",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
