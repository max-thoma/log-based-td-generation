from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Dimmable Color Light",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "OnOffSwitch",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A dimmable light that can be color controlled",
            "mqv:topic": "things/id-2",
            "properties": {
                "color": {
                    "name": "color",
                    "title": "Color",
                    "description": "The color of the light",
                    "type": "string",
                    "enum": [
                        "Aquamarine",
                        "CornflowerBlue	",
                        "Ivory",
                        "Red",
                        "SpringGreen",
                    ],  # random colors
                    "@type": "ColorProperty",
                    "readOnly": False,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-2/properties/color"},
                        {
                            "mqv:topic": "things/id-2/properties/color",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "colorTemperature": {
                    "name": "colorTemperature",
                    "value": 2500,
                    "title": "Color Temperature",
                    "description": "The currently set color temperature",
                    "type": "number",
                    "@type": "ColorTemperatureProperty",
                    "unit": "kelvin",
                    "minimum": 2500,
                    "maximum": 9000,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-2/properties/colorTemperature"},
                        {
                            "mqv:topic": "things/id-2/properties/colorTemperature",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "colorMode": {
                    "name": "colorMode",
                    "value": "color",
                    "title": "Color Mode",
                    "description": "There are two type of color modes, either the light is in mode 'color' or 'temperature'",
                    "type": "string",
                    "@type": "ColorModeProperty",
                    "enum": ["color", "temperature"],
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-2/properties/colorMode"},
                        {
                            "mqv:topic": "things/id-2/properties/colorMode",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "level": {
                    "name": "level",
                    "value": 0,
                    "title": "Brightness",
                    "description": "The current brightness level of the light form 0 to 100",
                    "type": "number",
                    "@type": "BrightnessProperty",
                    "unit": "percent",
                    "minimum": 0,
                    "maximum": 100,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-2/properties/level"},
                        {
                            "mqv:topic": "things/id-2/properties/level",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "on": {
                    "name": "on",
                    "value": False,
                    "title": "On/Off",
                    "description": "Indicated whethere the light is on or off",
                    "type": "boolean",
                    "@type": "OnOffProperty",
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-2/properties/on"},
                        {
                            "mqv:topic": "things/id-2/properties/on",
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
                    "mqv:topic": "things/id-2",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-2",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-2/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-2/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 3,
            "selectedCapability": "Light",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-2",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-2:readwrite",
                        "/things/id-2",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
