from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Temperature Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "TemperatureSensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that measures the air temperature",
            "mqv:topic": "things/id-17",
            "properties": {
                "temperature": {
                    "name": "temperature",
                    "value": 20,
                    "title": "Temperature",
                    "description": "The current temperature in degree celsius",
                    "type": "number",
                    "@type": "TemperatureProperty",
                    "unit": "degree celsius",
                    "minimum": -20,
                    "maximum": 50,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-17/properties/temperature"},
                        {
                            "mqv:topic": "things/id-17/properties/temperature",
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
                    "mqv:topic": "things/id-17",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-17",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-17/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-17/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 16,
            "selectedCapability": "TemperatureSensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-17",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-17:readwrite",
                        "/things/id-17",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
