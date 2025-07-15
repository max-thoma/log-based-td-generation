from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Video Camera",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "VideoCamera",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A network camera that can record videos",
            "mqv:topic": "things/id-20",
            "properties": {
                "video": {
                    "name": "video",
                    "value": "null",
                    "title": "Video",
                    "description": "The current video feed of the camera",
                    "type": "null",
                    "@type": "VideoProperty",
                    "readOnly": True,
                    "links": [
                        {
                            "rel": "alternate",
                            "mqv:topic": "media/id-20/index.mpd",
                            "mediaType": "application/dash+xml",
                        },
                        {
                            "rel": "alternate",
                            "mqv:topic": "media/id-20/master.m3u8",
                            "mediaType": "application/vnd.apple.mpegurl",
                        },
                    ],
                    "forms": [
                        {"mqv:topic": "things/id-20/properties/video"},
                        {
                            "mqv:topic": "things/id-20/properties/video",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                },
                "streamActive": {
                    "name": "streamActive",
                    "value": False,
                    "title": "Streaming",
                    "description": "This indicates if the camera stream is active",
                    "type": "boolean",
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-20/properties/streamActive"},
                        {
                            "mqv:topic": "things/id-20/properties/streamActive",
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
                    "mqv:topic": "things/id-20",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-20",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-20/properties",
                    "op": ["readallproperties", "writemultipleproperties"],
                },
                {
                    "mqv:topic": "things/id-20/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 18,
            "selectedCapability": "VideoCamera",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-20",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-20:readwrite",
                        "/things/id-20",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
