from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "title": "counter",
            "titles": {"en": "counter", "de": "zähler", "it": "Contatore"},
            "description": "counter example Thing",
            "descriptions": {
                "en": "counter example Thing",
                "de": "Zähler Beispiel Ding",
                "it": "Contatore Esempio",
            },
            "support": "git://github.com/eclipse/thingweb.node-wot.git",
            "@context": [
                "https://www.w3.org/2019/wot/td/v1",
                {"iot": "http://example.org/iot"},
                {"@language": "en"},
            ],
            "properties": {
                "count": {
                    "title": "Counter Value",
                    "type": "integer",
                    "description": "current counter value",
                    "descriptions": {
                        "en": "current counter value",
                        "de": "Derzeitiger Zähler Stand",
                        "it": "valore attuale del contatore",
                    },
                    "iot:Custom": "example annotation",
                    "observable": True,
                    "readOnly": True,
                    "writeOnly": False,
                    "forms": [
                        {
                            "mqv:topic": "counter/properties/count",
                            "contentType": "application/json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        },
                        {
                            "mqv:topic": "counter/properties/count/observable",
                            "contentType": "application/json",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "longpoll",
                        },
                        {
                            "mqv:topic": "coap://plugfest.thingweb.io:5683/counter/properties/count",
                            "contentType": "application/json",
                            "op": [
                                "readproperty",
                                "observeproperty",
                                "unobserveproperty",
                            ],
                        },
                    ],
                },
                "countAsImage": {
                    "title": "Counter SVG",
                    "description": "current counter value as SVG image",
                    "forms": [
                        {
                            "mqv:topic": "counter/properties/countAsImage{?fill}",
                            "contentType": "image/svg+xml",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        },
                        {
                            "mqv:topic": "coap://plugfest.thingweb.io:5683/counter/properties/countAsImage",
                            "contentType": "image/svg+xml",
                            "op": ["readproperty"],
                        },
                    ],
                    "observable": False,
                    "readOnly": True,
                    "uriVariables": {"fill": {"type": "string"}},
                    "writeOnly": False,
                },
                "lastChange": {
                    "type": "string",
                    "title": "Last Change",
                    "description": "last change of counter value",
                    "descriptions": {
                        "en": "last change of counter value",
                        "de": "Letzte Änderung",
                        "it": "ultima modifica del valore",
                    },
                    "observable": True,
                    "readOnly": True,
                    "writeOnly": False,
                    "forms": [
                        {
                            "mqv:topic": "counter/properties/lastChange",
                            "contentType": "application/json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                            "mock": lambda type, min, max, enum, name: [
                                "2025-05-01T11:14:25+00:00",
                                "2025-04-30T23:25:26+00:00",
                                "2025-04-30T22:21:59+00:00",
                                "2025-04-30T13:24:29+00:00",
                                "2025-04-29T14:24:21+00:00",
                            ],
                        },
                        {
                            "mqv:topic": "counter/properties/lastChange/observable",
                            "contentType": "application/json",
                            "op": ["observeproperty", "unobserveproperty"],
                            "subprotocol": "longpoll",
                        },
                        {
                            "mqv:topic": "coap://plugfest.thingweb.io:5683/counter/properties/lastChange",
                            "contentType": "application/json",
                            "op": [
                                "readproperty",
                                "observeproperty",
                                "unobserveproperty",
                            ],
                        },
                    ],
                },
            },
            "actions": {
                "increment": {
                    "title": "Increment Counter",
                    "description": "increment value",
                    "descriptions": {
                        "en": "increment value",
                        "de": "Zähler erhöhen",
                        "it": "incrementare valore",
                    },
                    "uriVariables": {
                        "step": {"type": "integer", "minimum": 1, "maximum": 250}
                    },
                    "forms": [
                        {
                            "mqv:topic": "counter/actions/increment{?step}",
                            "contentType": "application/json",
                            "op": ["invokeaction"],
                            "htv:methodName": "POST",
                        },
                        {
                            "mqv:topic": "coap://plugfest.thingweb.io:5683/counter/actions/increment",
                            "contentType": "application/json",
                            "op": ["invokeaction"],
                        },
                    ],
                    "idempotent": False,
                    "safe": False,
                },
                "decrement": {
                    "title": "Decrement Counter",
                    "description": "decrement value",
                    "descriptions": {
                        "en": "decrement value",
                        "de": "Zähler verringern",
                        "it": "decrementare valore",
                    },
                    "uriVariables": {
                        "step": {"type": "integer", "minimum": 1, "maximum": 250}
                    },
                    "forms": [
                        {
                            "mqv:topic": "counter/actions/decrement{?step}",
                            "contentType": "application/json",
                            "op": ["invokeaction"],
                            "htv:methodName": "POST",
                        },
                        {
                            "mqv:topic": "coap://plugfest.thingweb.io:5683/counter/actions/decrement",
                            "contentType": "application/json",
                            "op": ["invokeaction"],
                        },
                    ],
                    "idempotent": False,
                    "safe": False,
                },
                "reset": {
                    "title": "Reset Counter",
                    "description": "Resetting counter value",
                    "descriptions": {
                        "en": "Resetting counter value",
                        "de": "Zähler resettieren",
                        "it": "resettare valore",
                    },
                    "forms": [
                        {
                            "mqv:topic": "counter/actions/reset",
                            "contentType": "application/json",
                            "op": ["invokeaction"],
                            "htv:methodName": "POST",
                        },
                        {
                            "mqv:topic": "coap://plugfest.thingweb.io:5683/counter/actions/reset",
                            "contentType": "application/json",
                            "op": ["invokeaction"],
                        },
                    ],
                    "idempotent": False,
                    "safe": False,
                },
            },
            "events": {
                "change": {
                    "title": "Change Event",
                    "description": "change event",
                    "descriptions": {
                        "en": "change event",
                        "de": "Änderungsnachricht",
                        "it": "resettare valore",
                    },
                    "forms": [
                        {
                            "mqv:topic": "counter/events/change",
                            "contentType": "application/json",
                            "subprotocol": "longpoll",
                            "op": ["subscribeevent", "unsubscribeevent"],
                        },
                        {
                            "mqv:topic": "ws://plugfest.thingweb.io:8083/counter/events/change",
                            "contentType": "application/json",
                            "op": ["subscribeevent"],
                        },
                        {
                            "mqv:topic": "coap://plugfest.thingweb.io:5683/counter/events/change",
                            "contentType": "application/json",
                            "op": ["subscribeevent", "unsubscribeevent"],
                        },
                    ],
                }
            },
            "@type": "CounterThing",
            "security": ["nosec_sc"],
            "id": "urn:uuid:fc6dafae-b2df-4fa1-ac43-b6466d03bc38",
            "forms": [
                {
                    "mqv:topic": "counter/all/properties",
                    "contentType": "application/json",
                    "op": ["readallproperties", "readmultipleproperties"],
                }
            ],
            "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
        }
    )
