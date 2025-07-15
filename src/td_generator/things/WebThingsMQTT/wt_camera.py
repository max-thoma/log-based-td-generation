from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Camera",
            "description": "A camera that periodically takes pictures",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "Camera",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "mqv:topic": "things/id-19",
            "properties": {
                "image": {
                    "name": "image",
                    "value": "null",
                    "title": "Image",
                    "description": "The latest picture taken by the camera",
                    "type": "null",
                    "@type": "ImageProperty",
                    "readOnly": True,
                    "links": [
                        {
                            "rel": "alternate",
                            "mqv:topic": "media/id-19/image.png",
                            "mediaType": "image/png",
                        }
                    ],
                    "forms": [
                        {"mqv:topic": "things/id-19/properties/image"},
                        {
                            "mqv:topic": "things/id-19/properties/image",
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
                    "mqv:topic": "things/id-19",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-19",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-19/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-19/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 17,
            "selectedCapability": "Camera",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-19",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-19:readwrite",
                        "/things/id-19",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
