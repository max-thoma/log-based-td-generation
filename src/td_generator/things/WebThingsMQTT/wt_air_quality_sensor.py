from td import ThingDescription


def td():
    return ThingDescription(
        **{
            "title": "Air Quality Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "AirQualitySensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that measure the air quality",
            "mqv:topic": "things/id-28",
            "properties": {
                "concentration": {
                    "name": "concentration",
                    "value": 20,
                    "title": "Gas Concentration",
                    "description": "The measured gas concentration",
                    "type": "number",
                    "@type": "ConcentrationProperty",
                    "unit": "ppm",
                    "minimum": 0,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-28/properties/concentration"},
                        {
                            "mqv:topic": "things/id-28/properties/concentration",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "density": {
                    "name": "density",
                    "value": 20,
                    "title": "Particulate Density",
                    "description": "The measured particulate density",
                    "type": "number",
                    "@type": "DensityProperty",
                    "unit": "micrograms per cubic metre",
                    "minimum": 0,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-28/properties/density"},
                        {
                            "mqv:topic": "things/id-28/properties/density",
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
                    "mqv:topic": "things/id-28",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-28",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-28/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-28/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 26,
            "selectedCapability": "AirQualitySensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-28",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-28:readwrite",
                        "/things/id-28",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
