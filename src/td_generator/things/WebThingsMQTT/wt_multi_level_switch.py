from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Multi-level Switch",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "MultiLevelSwitch",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A switch that can measure levels",
            "mqv:topic": "things/id-1",
            "properties": {
                "level": {
                    "name": "level",
                    "value": 0,
                    "title": "Level",
                    "description": "The currently level as measured by the switch",
                    "type": "number",
                    "@type": "LevelProperty",
                    "unit": "percent",
                    "minimum": 0,
                    "maximum": 100,
                    "readOnly": False,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-1/properties/level"},
                        {
                            "mqv:topic": "things/id-1/properties/level",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "on": {
                    "name": "on",
                    "value": False,
                    "title": "On/Off",
                    "type": "boolean",
                    "description": "Indicates the on/off state of the switch",
                    "@type": "OnOffProperty",
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-1/properties/on"},
                        {
                            "mqv:topic": "things/id-1/properties/on",
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
                    "mqv:topic": "things/id-1",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-1",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-1/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-1/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 2,
            "selectedCapability": "MultiLevelSwitch",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-1",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-1:readwrite",
                        "/things/id-1",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
