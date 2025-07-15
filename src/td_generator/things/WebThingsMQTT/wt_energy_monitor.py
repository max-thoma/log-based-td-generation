from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Energy Monitor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "EnergyMonitor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A device that measures and monitors energy consumption",
            "mqv:topic": "things/id-22",
            "properties": {
                "instantaneousPower": {
                    "name": "instantaneousPower",
                    "value": 0,
                    "title": "Power",
                    "description": "The current power draw in watts",
                    "type": "number",
                    "@type": "InstantaneousPowerProperty",
                    "unit": "watt",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-22/properties/instantaneousPower"},
                        {
                            "mqv:topic": "things/id-22/properties/instantaneousPower",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "instantaneousPowerFactor": {
                    "name": "instantaneousPowerFactor",
                    "value": 0,
                    "title": "Power Factor",
                    "description": "The measured power factor",
                    "type": "number",
                    "@type": "InstantaneousPowerFactorProperty",
                    "minimum": -1,
                    "maximum": 1,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {
                            "mqv:topic": "things/id-22/properties/instantaneousPowerFactor"
                        },
                        {
                            "mqv:topic": "things/id-22/properties/instantaneousPowerFactor",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "voltage": {
                    "name": "voltage",
                    "value": 0,
                    "title": "Voltage",
                    "description": "The current line voltage",
                    "type": "number",
                    "@type": "VoltageProperty",
                    "unit": "volt",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-22/properties/voltage"},
                        {
                            "mqv:topic": "things/id-22/properties/voltage",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "current": {
                    "name": "current",
                    "value": 0,
                    "title": "Current",
                    "description": "The measured current draw in amps",
                    "type": "number",
                    "@type": "CurrentProperty",
                    "unit": "ampere",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-22/properties/current"},
                        {
                            "mqv:topic": "things/id-22/properties/current",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "frequency": {
                    "name": "frequency",
                    "value": 0,
                    "title": "Frequency",
                    "description": "The current mesaured AC frequency",
                    "type": "number",
                    "@type": "FrequencyProperty",
                    "unit": "hertz",
                    "minimum": 59,
                    "maximum": 61,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-22/properties/frequency"},
                        {
                            "mqv:topic": "things/id-22/properties/frequency",
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
                    "mqv:topic": "things/id-22",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-22",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-22/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-22/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 20,
            "selectedCapability": "EnergyMonitor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-22",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-22:readwrite",
                        "/things/id-22",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
