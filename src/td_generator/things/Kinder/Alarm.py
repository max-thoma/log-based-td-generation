from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@context": ["https://www.w3.org/2019/wot/td/v1"],
            "id": "alarm",
            "title": "Alarm",
            "description": "An alarm clock with acoustic and vibration wake functionality.",
            "@type": "Alarm",
            "base": "http://127.0.0.1:5000",
            "owl:sameAs": "test",
            "securityDefinitions": {"basic_sc": {"scheme": "basic", "in": "header"}},
            "security": ["basic_sc"],
            "properties": {
                "set": {
                    "type": "boolean",
                    "title": "Alarm Set",
                    "description": "Indicates whether alarm is currently set or not",
                    "forms": [
                        {
                            "mqv:topic": "alarm/is_set",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "vibration": {
                    "type": "boolean",
                    "title": "Vibration Enabled",
                    "description": "States whether the alarm is set to vibration only mode",
                    "forms": [
                        {
                            "mqv:topic": "alarm/vibration_enabled",
                            "mediaType": "application/Json",
                            "op": ["readproperty"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
            "actions": {
                "set alarm": {
                    "title": "Set Alarm",
                    "description": "Sets alarm, ringing or vibration at the set time",
                    "forms": [
                        {
                            "mqv:topic": "alarm/set",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "unset": {
                    "title": "Unset Alarm",
                    "description": "Unsets alarm",
                    "forms": [
                        {
                            "mqv:topic": "alarm/unset",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
                "toggle vibration mode": {
                    "title": "Toggle Vibration",
                    "description": "Switches vibration only mode on or off depending on the current setting.",
                    "forms": [
                        {
                            "mqv:topic": "alarm/toggle",
                            "contentType": "application/Json",
                            "op": ["invokeaction"],
                            "htv:methodName": "GET",
                        }
                    ],
                },
            },
        }
    )
