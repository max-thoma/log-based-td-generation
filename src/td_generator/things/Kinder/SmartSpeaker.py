from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "speaker",
            "title": "smart speaker",
            "@type": "Wireless Online Speaker",
            "description": "Smart speaker with a wireless internet connection",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "connection": {
                    "type": "boolean",
                    "title": "Online Connection Status",
                    "description": "States whether the speaker is connected to the Internet or not. If False music can not be played and the speaker must first be reconnected to the network",
                    "forms": [
                        {
                            "mqv:topic": "speaker/is_connected",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "playing": {
                    "title": "Speaker Active",
                    "type": "boolean",
                    "description": "States whether the speaker is currently playing music or not",
                    "forms": [
                        {
                            "mqv:topic": "speaker/is_playing",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "status": {
                    "title": "Speaker Status",
                    "type": "boolean",
                    "description": "Indicates if the speaker is currently switched on or off",
                    "forms": [
                        {
                            "mqv:topic": "speaker/status",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "volume": {
                    "title": "Volume Level",
                    "type": "integer",
                    "minimum": 10,
                    "maximum": 120,
                    "description": "The speaker volume in db",
                    "forms": [
                        {
                            "mqv:topic": "speaker/volume",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "reconnect": {
                    "title": "Reconnect Speaker",
                    "description": "Reconnects device with the internet, enabling music to be played if connection was lost",
                    "forms": [
                        {
                            "mqv:topic": "speaker/reconnect",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "play": {
                    "title": "Start Playback",
                    "description": "Starts playing music from the selected player",
                    "forms": [
                        {
                            "mqv:topic": "speaker/play",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "pause": {
                    "title": "Stop Playback",
                    "description": "Pauses music if currently playing",
                    "forms": [
                        {
                            "mqv:topic": "speaker/pause",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "toggle": {
                    "title": "Toggle Power",
                    "description": "Turn the speaker on of off",
                    "forms": [
                        {
                            "mqv:topic": "speaker/toggle",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "standby": {
                    "title": "Go To Standby",
                    "description": "Puts the device into standby, making it unavailable",
                    "forms": [
                        {
                            "mqv:topic": "speaker/standby",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "change player": {
                    "title": "Change Streaming Service",
                    "description": "Changes music streaming service.",
                    "forms": [
                        {
                            "mqv:topic": "speaker/change_player",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "increase volume": {
                    "title": "Increase Volume",
                    "description": "Increases the volume by 5 db",
                    "forms": [
                        {
                            "mqv:topic": "speaker/increase_volume",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "decrease volume": {
                    "title": "Decrease Volume",
                    "description": "Decreases volume by 5 db",
                    "forms": [
                        {
                            "mqv:topic": "speaker/decrease_volume",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
