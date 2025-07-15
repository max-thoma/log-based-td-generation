from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "Alarm",
            "@context": [
                "https://www.w3.org/2022/wot/td/v1.1",
                "https://webthings.io/schemas",
            ],
            "@type": "Alarm",
            "profile": [
                "https://www.w3.org/2022/wot/profile/http-basic/v1",
                "https://www.w3.org/2022/wot/profile/http-sse/v1",
            ],
            "description": "An alarm system that can be remotely be triggered and silenced",
            "mqv:topic": "things/id-21",
            "properties": {
                "alarm": {
                    "name": "alarm",
                    "value": False,
                    "title": "Alarm",
                    "description": "This property indicates whether the alarm is on or off",
                    "type": "boolean",
                    "@type": "AlarmProperty",
                    "readOnly": True,
                    "links": [],
                    "forms": [
                        {"mqv:topic": "things/id-21/properties/alarm"},
                        {
                            "mqv:topic": "things/id-21/properties/alarm",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "sse",
                        },
                    ],
                }
            },
            "actions": {
                "trigger": {
                    "title": "Trigger",
                    "description": "Trigger the alarm",
                    "forms": [{"mqv:topic": "things/id-21/actions/trigger"}],
                },
                "silence": {
                    "title": "Silence",
                    "description": "Silence the alarm",
                    "forms": [{"mqv:topic": "things/id-21/actions/silence"}],
                },
            },
            "events": {
                "alarmEvent": {
                    "title": "Alarm",
                    "description": "This event is emitted when the alarm is triggered",
                    "@type": "AlarmEvent",
                    "readOnly": True,
                    "data": {"type": "string", "enum": ["ALARM"]},
                    "forms": [
                        {
                            "mqv:topic": "things/id-21/events/alarmEvent",
                            "subprotocol": "sse",
                        }
                    ],
                }
            },
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "mqv:topic": "things/id-21",
                },
                {
                    "rel": "alternate",
                    "mqv:topic": "wss://plugfest.webthings.io/things/id-21",
                },
            ],
            "forms": [
                {
                    "mqv:topic": "things/id-21/properties",
                    "op": "readallproperties",
                },
                {
                    "mqv:topic": "things/id-21/properties",
                    "op": ["observeallproperties", "unobserveallproperties"],
                    "subprotocol": "sse",
                },
                {
                    "mqv:topic": "things/id-21/actions",
                    "op": "queryallactions",
                },
                {
                    "mqv:topic": "things/id-21/events",
                    "op": ["subscribeallevents", "unsubscribeallevents"],
                    "subprotocol": "sse",
                },
            ],
            "layoutIndex": 19,
            "selectedCapability": "Alarm",
            "iconHref": "null",
            "group_id": "null",
            "id": "https://plugfest.webthings.io/things/id-21",
            "base": "https://plugfest.webthings.io/",
            "securityDefinitions": {
                "oauth2_sc": {
                    "scheme": "oauth2",
                    "flow": "code",
                    "authorization": "https://plugfest.webthings.io/oauth/authorize",
                    "token": "https://plugfest.webthings.io/oauth/token",
                    "scopes": [
                        "/things/id-21:readwrite",
                        "/things/id-21",
                        "/things:readwrite",
                        "/things",
                    ],
                }
            },
            "security": "oauth2_sc",
        }
    )
