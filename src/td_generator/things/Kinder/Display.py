from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": [
                "https://www.w3.org/2019/wot/td/v1",
                {"saref": "https://w3id.org/saref#"},
            ],
            "id": "urn:dev:ops:WoTDisp-0001",
            "title": "MyDispThing",
            "description": "A smart display than can display text, videos, news and web apps.",
            "@type": "saref:Device",
            "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
            "security": ["nosec_sc"],
            "base": "http://192.168.30.121:8888/",
            "properties": {
                "power": {
                    "title": "Power",
                    "description": "Current power status of the Smart Display",
                    "type": "object",
                    "properties": {"status": {"type": "boolean"}},
                    "forms": [
                        {
                            "op": ["readproperty"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "power",
                            "mock": lambda type, min, max, enum, name: [
                                {"status": True},
                                {"status": True},
                                {"status": False},
                                {"status": True},
                                {"status": False},
                            ],
                        }
                    ],
                },
                "content": {
                    "title": "Available Content",
                    "description": "A list of available content that can be displayed",
                    "type": "string",
                    "forms": [
                        {
                            "op": ["readproperty"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "content",
                            "mock": lambda type, min, max, enum, name: [
                                "Video_1.mp4",
                                "Picture_2022.jpeg",
                                "Chanel A",
                                "Sales.txt",
                            ],
                        }
                    ],
                },
            },
            "actions": {
                "toggle": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Toggle Power Status",
                    "description": "Toggle the Power Status of the Smart Display",
                    "@type": "saref:ToggleCommand",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "toggle",
                        }
                    ],
                },
                "setVolume": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Set Volume",
                    "description": "Set the volume level",
                    "@type": "saref:Level control function",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "setvolume",
                        }
                    ],
                },
                "setBright": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Set Brightness",
                    "description": "Set the brightness level of the pannel",
                    "@type": "saref:Level control function",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "setbright",
                        }
                    ],
                },
                "showText": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Show Text",
                    "description": "Display a text file on the Smart Display",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "showtext",
                        }
                    ],
                },
                "playVideo": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Play Video",
                    "description": "Start playing a video from the network",
                    "type": "playVOD",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "playvideo",
                            "mock": lambda type, min, max, enum, name: [
                                {
                                    "identifier": "advert-1",
                                    "name": "Advert for Product 1",
                                    "description": "An advertisement for product 1",
                                    "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                                },
                                {
                                    "identifier": "store-tour",
                                    "name": "Store Tour",
                                    "description": "Tour around the store",
                                    "url": "http://192.168.0.70:3000/videos/store.mp4",
                                },
                                {
                                    "identifier": "sale",
                                    "name": "Sales",
                                    "description": "Video promoting the Black Friday sale",
                                    "url": "http://192.168.0.70:3000/videos/bf_sale_2025.mp4",
                                },
                            ],
                        }
                    ],
                    "input": {
                        "type": "object",
                        "properties": {
                            "identifier": {"type": "string"},
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "url": {"type": "string"},
                        },
                    },
                },
                "pauseVideo": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Pause Video",
                    "description": "Pause the current video playback",
                    "type": "pauseVOD",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "pausevideo",
                        }
                    ],
                },
                "stopVideo": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Stop Video",
                    "type": "stopVOD",
                    "description": "Stop the current video playback",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "stopvideo",
                        }
                    ],
                },
                "presentationWebApp": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Presentation Web App",
                    "type": "presentationWebApp",
                    "description": "Open and display a preconfigured Web App",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "presentationwebapp",
                            "mock": lambda type, min, max, enum, name: [
                                {
                                    "identifier": "facebook",
                                    "name": "Facebook Page",
                                    "description": "The Facebook page of the store",
                                    "url": "www.facebook.com",
                                },
                                {
                                    "identifier": "yelp",
                                    "name": "Yelp Page",
                                    "description": "The Yelp Review Page",
                                    "url": "www.yelp.com",
                                },
                                {
                                    "identifier": "google",
                                    "name": "Google Store Page",
                                    "description": "The Google reviews page of the store",
                                    "url": "www.google.com",
                                },
                            ],
                        }
                    ],
                    "input": {
                        "type": "object",
                        "properties": {
                            "identifier": {"type": "string"},
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "url": {"type": "string"},
                        },
                    },
                },
                "launchNewsApp": {
                    "safe": True,
                    "idempotent": False,
                    "title": "Launch News App",
                    "description": "Launch the preconfigured new app",
                    "forms": [
                        {
                            "op": ["invokeaction"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "launchnewsapp",
                        }
                    ],
                },
            },
            "events": {
                "weatherAlert": {
                    "title": "Weather Alert",
                    "description": "The Smart Display can display and warn about weather events",
                    "data": {
                        "type": "object",
                        "properties": {
                            "region": {"type": "string"},
                            "alert": {"type": "string"},
                        },
                    },
                    "forms": [
                        {
                            "op": ["subscribeevent"],
                            "contentType": "application/json;charset=utf-8",
                            "subprotocol": "longpoll",
                            "mqv:topic": "weatheralert",
                            "mock": lambda type, min, max, enum, name: [
                                {"region": "TX, Houston", "alert": "Rainstorm"},
                                {"region": "FL, Tampa", "alert": "Ice storm"},
                                {
                                    "region": "CA, San Jose",
                                    "alert": "Heat wave",
                                },
                                {"region": "MI, Detroit", "alert": "Heavy winds"},
                            ],
                        },
                        {
                            "op": ["subscribeevent"],
                            "contentType": "application/json;charset=utf-8",
                            "mqv:topic": "ws://192.168.30.121:8888/weatheralert",
                        },
                    ],
                }
            },
        }
    )
