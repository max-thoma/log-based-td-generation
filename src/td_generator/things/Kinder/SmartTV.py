from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "tv",
            "title": "Smart TV",
            "@type": "Entertainment device",
            "description": "A smart Television with recording capabilities",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "recording": {
                    "type": "boolean",
                    "title": "Recording Enabled",
                    "description": "True if the TV is currently recording the selected channel",
                    "forms": [
                        {
                            "mqv:topic": "tv/is_recording",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "off": {
                    "type": "boolean",
                    "title": "TV Off",
                    "description": "Indicates if the TV is turned off(True) or turned on (False)",
                    "forms": [
                        {
                            "mqv:topic": "tv/is_off",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "brightness": {
                    "type": "integer",
                    "title": "Brightness Level",
                    "description": "Describes brightness of the TV screen in percent",
                    "minimum": 0,
                    "maximum": 100,
                    "forms": [
                        {
                            "mqv:topic": "tv/brightness",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "channel": {
                    "type": "string",
                    "title": "Current Channel",
                    "description": "States the currently selected channel that will be displayed if the device is turned on",
                    "characteristics": ["PRO7", "RTL", "SAT1", "ARD", "ZDF", "KIKA"],
                    "enum": ["PRO7", "RTL", "SAT1", "ARD", "ZDF", "KIKA"],
                    "forms": [
                        {
                            "mqv:topic": "tv/channel",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "record": {
                    "title": "Start Recording",
                    "description": "Starts recording the current channel",
                    "forms": [
                        {
                            "mqv:topic": "tv/record",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "switch": {
                    "title": "Switch Channels",
                    "description": "Switches to a different channel",
                    "forms": [
                        {
                            "mqv:topic": "tv/switch",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "turn on": {
                    "title": "Turn On",
                    "description": "Turns the TV on",
                    "forms": [
                        {
                            "mqv:topic": "tv/turn_on",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "turn off": {
                    "title": "Turn Off",
                    "description": "Turns the TV off",
                    "forms": [
                        {
                            "mqv:topic": "tv/turn_off",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "set brightness": {
                    "title": "Set Brightness Level",
                    "description": "Sets the brightness of the tv.",
                    "forms": [
                        {
                            "mqv:topic": "tv/set_brightness",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "PUT",
                        }
                    ],
                    "input": {"type": "integer", "minimum": 0, "maximum": 100},
                },
            },
        }
    )
