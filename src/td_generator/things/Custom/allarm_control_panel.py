from td import ThingDescription

def td():
    return ThingDescription(
        **{
            "@type": "HouseAlarm",
            "title": "Alarm Control Panel",
            "id": "urn:uuid:b9ce7480-3a89-4eb7-8754-e4bb6462f893",
            "description": "The alarm control panel of the house",
            "securityDefinitions": {"nosec_sc": {"scheme": "nosec"}},
            "security": ["nosec_sc"],
            "properties": {
                "state": {
                    "title": "Alarm System State",
                    "description": "The current state of the alarm system",
                    "observable": True,
                    "type": "string",
                    "enum": [
                        "disarmed",
                        "armed_home",
                        "armed_away",
                        "armed_night",
                        "armed_vacation",
                        "armed_custom_bypass",
                        "pending",
                        "triggered",
                    ],
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "mqv:topic": "home/alarm",
                            "mqv:retain": True,
                            "op": ["observeproperty", "readproperty"],
                        }
                    ],
                }
            },
            "actions": {
                "arm": {
                    "title": "Arm",
                    "description": "Arm or disarm the alarm system",
                    "input": {
                        "observable": True,
                        "type": "string",
                        "enum": [
                            "DISARM",
                            "ARM_HOME",
                            "ARM_AWAY",
                            "ARM_NIGHT",
                            "ARM_VACATION",
                            "ARM_CUSTOM_BYPASS",
                        ],
                        "forms": [],
                    },
                    "forms": [
                        {
                            "href": "192.168.0.100:1883",
                            "contentType": "text/plain",
                            "response": {"contentType": "text/plain"},
                            "mqv:topic": "home/alarm/set",
                            "mqv:retain": False,
                            "op": ["invokeaction"],
                        }
                    ],
                }
            },
        }
    )
