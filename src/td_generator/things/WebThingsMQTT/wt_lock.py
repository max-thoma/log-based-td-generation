from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Lock",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "Lock",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "A look that can be remotely opened and closed",
            "mqv:topic": "things/id-25",
            "properties": {
                "locked": {
                    "name": "locked",
                    "value": "unlocked",
                    "title": "Current State",
                    "description": "The current state of the lock. It can either be locked, unlocked, jammed or unknown",
                    "type": "string",
                    "@type": "LockedProperty",
                    "enum": ["locked", "unlocked", "jammed", "unknown"],
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-25/properties/locked"},
                        {
                            "mqv:topic": "things/id-25/properties/locked",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                }
            },
            "actions": {
                "lock": {
                    "@type": "LockAction",
                    "title": "Lock",
                    "description": "Lock the locking mechanism",
                    "forms": [{"mqv:topic": "things/id-25/actions/lock"}],
                },
                "unlock": {
                    "@type": "UnlockAction",
                    "title": "Unlock",
                    "description": "Unlock the locking mechanism",
                    "forms": [{"mqv:topic": "things/id-25/actions/unlock"}],
                },
            },
            "events": {},
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "mqv:topic": "things/id-25",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-25",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-25/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-25/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
                {
                    "mqv:topic": "things/id-25/actions",
                    "op": "queryallactions",
                },
            ],
            "layoutIndex": 23,
            "selectedCapability": "Lock",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-25",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-25:readwrite",
                        "/things/id-25",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
