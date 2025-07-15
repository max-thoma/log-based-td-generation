from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "radio",
            "title": "Smart radio device",
            "description": "A radio with remote chanel switching",
            "@type": "Radio",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "power": {
                    "title": "Current Operation Status",
                    "type": "string",
                    "description": "Power status indicating if the device is turned on or off",
                    "characteristics": ["off", "on"],
                    "enum": ["on", "off"],
                    "forms": [
                        {
                            "mqv:topic": "radio/power",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "channel": {
                    "type": "string",
                    "title": "Current Radio Channel",
                    "description": "Displays the current channel of the radio",
                    "characteristics": ["MTV", "Jamz", "The Beat", "The Mix"],
                    "enum": ["MTV", "Jamz", "The Beat", "The Mix"],
                    "forms": [
                        {
                            "mqv:topic": "radio/channel",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "power on": {
                    "title": "Power On Radio",
                    "description": "Turns the radio on",
                    "forms": [
                        {
                            "mqv:topic": "radio/power_on",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "switch channel": {
                    "title": "Switch Channel",
                    "description": "Switches channel of the radio to the next available channel",
                    "forms": [
                        {
                            "mqv:topic": "radio/switch_channel",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "power off": {
                    "title": "Power Off Radio",
                    "description": "Turns the radio off",
                    "forms": [
                        {
                            "mqv:topic": "radio/power_off",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
