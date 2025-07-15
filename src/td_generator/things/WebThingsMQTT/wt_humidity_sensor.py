from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Humidity Sensor",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "HumiditySensor",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A sensor that measures the air humidity",
            "mqv:topic": "things/id-27",
            "properties": {
                "humidity": {
                    "name": "humidity",
                    "value": 20,
                    "title": "Humidity",
                    "description": "The currently measures humidity in percent",
                    "type": "number",
                    "@type": "HumidityProperty",
                    "unit": "percent",
                    "minimum": 0,
                    "maximum": 100,
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-27/properties/humidity"},
                        {
                            "mqv:topic": "things/id-27/properties/humidity",
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
                    "mqv:topic": "things/id-27",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-27",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-27/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-27/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 25,
            "selectedCapability": "HumiditySensor",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-27",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-27:readwrite",
                        "/things/id-27",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
