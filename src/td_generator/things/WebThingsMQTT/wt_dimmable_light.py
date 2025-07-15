from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Dimmable Light",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "OnOffSwitchLight",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A light with adjustable brightness",
            "mqv:topic": "things/id-8",
            "properties": {
                "on": {
                    "name": "on",
                    "value": False,
                    "title": "On/Off",
                    "description": "The current on/off state of the light as boolean value",
                    "type": "boolean",
                    "@type": "OnOffProperty",
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-8/properties/on"},
                        {
                            "mqv:topic": "things/id-8/properties/on",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "level": {
                    "name": "level",
                    "value": 0,
                    "title": "Brightness",
                    "description": "The brightness level of the light in the range of 0 to 100",
                    "type": "number",
                    "@type": "BrightnessProperty",
                    "unit": "percent",
                    "minimum": 0,
                    "maximum": 100,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-8/properties/level"},
                        {
                            "mqv:topic": "things/id-8/properties/level",
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
                    "mqv:topic": "things/id-8",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-8",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-8/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-8/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 9,
            "selectedCapability": "Light",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-8",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-8:readwrite",
                        "/things/id-8",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
