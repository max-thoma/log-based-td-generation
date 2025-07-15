from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "On/Off Color Temperature Light",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "LightColorControl",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A light bulb that with color temperature controls",
            "mqv:topic": "things/id-12",
            "properties": {
                "on": {
                    "name": "on",
                    "value": False,
                    "title": "On/Off",
                    "description": "The operational state of the light, indicating if its turned on or off",
                    "type": "boolean",
                    "@type": "OnOffProperty",
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-12/properties/on"},
                        {
                            "mqv:topic": "things/id-12/properties/on",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "colorTemperature": {
                    "name": "colorTemperature",
                    "value": 2500,
                    "title": "Color Temperature",
                    "description": "The current color temperature of the light",
                    "type": "number",
                    "@type": "ColorTemperatureProperty",
                    "unit": "kelvin",
                    "minimum": 2500,
                    "maximum": 9000,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-12/properties/colorTemperature"},
                        {
                            "mqv:topic": "things/id-12/properties/colorTemperature",
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
                    "mqv:topic": "things/id-12",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-12",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-12/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-12/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 11,
            "selectedCapability": "Light",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-12",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-12:readwrite",
                        "/things/id-12",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
