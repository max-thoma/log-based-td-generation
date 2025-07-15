from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Barometric Pressure Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "BarometricPressureSensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that measures the barometric pressure aka. the atmospheric pressure",
            "mqv:topic": "things/id-29",
            "properties": {
                "pressure": {
                    "name": "pressure",
                    "value": 20,
                    "title": "Pressure",
                    "description": "The barometric pressure as measured by the sensor in hectopascal",
                    "type": "number",
                    "@type": "BarometricPressureProperty",
                    "unit": "hectopascal",
                    "minimum": 0,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-29/properties/pressure"},
                        {
                            "mqv:topic": "things/id-29/properties/pressure",
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
                    "mqv:topic": "things/id-29",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-29",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-29/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-29/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 27,
            "selectedCapability": "BarometricPressureSensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-29",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-29:readwrite",
                        "/things/id-29",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
